import arviz as az
import pymc3 as pm


def make_rayquaza_model():
    with pm.Model() as model:
        p_shiny = pm.Beta("p_shiny", 1, 2)
        n_shinies = pm.Binomial(
            "number_of_shinies", 44, p_shiny, observed=2,
        )

    return model


def sample(model: pm.Model) -> az.InferenceData:
    with model:
        mcmc = pm.sample(draws=1000, tune=500, chains=4)
        idata = az.from_pymc3(mcmc)

    return idata


# visualizing priors
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
pal = sns.color_palette("Set2")


def make_prior_plots():
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].hist(
        pm.Beta.dist(1, 3).random(size=10000), color=pal[0],
    )
    ax[1].hist(
        pm.Beta.dist(1, 8).random(size=10000), color=pal[1],
    )
    ax[2].hist(
        pm.Uniform.dist(0, 0.5).random(size=10000),
        color=pal[3],
    )
    ax[2].set_xlim(0, 1)
    ax[0].set_title("Beta(1, 3)")
    ax[1].set_title("Beta(1, 8)")
    ax[2].set_title("Uniform(0, 0.5)")
    fig.suptitle("Three possible priors for p_shiny")


def prior_predictive_checks(model: pm.Model):
    ppc = pm.sample_prior_predictive(model)
    print(f"Keys: {ppc.keys()}")
    print(f"Shape: {ppc['number-of-shinies'].shape}")
    return ppc


def plot_ppc():
    prior = prior_predictive_checks(make_rayquaza_model())
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].hist(
        prior["p_shiny"], color=pal[0],
    )
    ax[1].hist(
        prior["number_of_shinies"], color=pal[1],
    )
    ax[0].set_title("Prior for p_shiny")
    ax[1].set_title("Prior for # of shinies")


if __name__ == "__main__":
    model = make_rayquaza_model()
    ray_samples = sample(model)

