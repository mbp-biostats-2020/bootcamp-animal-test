# Mammalian sleep data

This is an updated and expanded version of the mammals sleep dataset.
Updated sleep times and weights were taken from V. M. Savage and G. B. West.
A quantitative, theoretical framework for understanding mammalian sleep.
Proceedings of the National Academy of Sciences, 104 (3):1051-1056, 2007.

## Data description

A data frame with 83 rows and 11 variables:

| Column name    | Description                           |
| -------------- | ------------------------------------- |
| `name`         | common name                           |
| `genus`        |                                       |
| `vore`         | what type of food the animal eats     |
| `order`        |                                       |
| `conservation` | the conservation status of the animal |
| `sleep_total`  | total amount of sleep, in hours       |
| `sleep_rem`    | rem sleep, in hours                   |
| `sleep_cycle`  | length of sleep cycle, in hours       |
| `awake`        | amount of time spent awake, in hours  |
| `brainwt`      | brain weight in kilograms             |
| `bodywt`       | body weight in kilograms              |

### Conservation status acronyms

| Status                 | Short form | Description                                                                                                           |
| ---------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------- |
| Extinct                | `EX`       | No known living individuals                                                                                           |
| Extinct in the wild    | `EW`       | Known only to survive in captivity, or as a naturalized population outside its historic range                         |
| Critically endangered  | `CR`       | Extremely high risk of extinction in the wild                                                                         |
| Endangered             | `EN`       | High risk of extinction in the wild                                                                                   |
| Vulnerable             | `VU`       | High risk of endangerment in the wild                                                                                 |
| Near threatened        | `NT`       | Likely to become endangered in the near future                                                                        |
| Least concern          | `LC`       | Lowest risk; does not qualify for a higher risk category. Widespread and abundant taxa are included in this category. |
| Conservation-dependent | `CD`       | Lowest risk;  dependent on conservation efforts to prevent it from becoming threatened with extinction.               |
| Data deficient         | `DD`       | Not enough data to make an assessment of its risk of extinction                                                       |
| Not evaluated          | `NE`       | Has not yet been evaluated against the criteria.                                                                      |
