
# Income Distribution Analysis Using Statistical Physics

## A Study of Low, Medium, and High-Income Society Classes

### M. Jagielski, R. Kutner

---

## Introduction

For over two decades, physicists have been using statistical physics to explain economic processes, particularly focusing on income distribution. This paper aims to describe the mechanisms of societies' enrichment or impoverishment using methods of statistical physics.

**Historical Context:**

- Vilfredo Pareto discovered the weak Pareto law.

- Robert Gibrat proposed the Rule of Proportionate Growth.

---

## Objectives

- **Study Three Classes:** Unlike previous studies that focused on two classes (low and medium income), this paper includes a high-income class as well.

- **Unified Formula:** Derive a formula that accurately describes income distribution across all three classes.

- **Empirical Validation:** Validate the model using income data from the European Union for the years 2006 and 2008.

**Key Challenges:**

1. Develop a unified formula to describe household incomes for all society classes.

2. Provide a microscopic mechanism responsible for the income structure and dynamics.

---

## Methodology

The study uses data from the Eurostat Survey on Income and Living Conditions (EU-SILC) and billionaire data from the Forbes list. The methodology is based on nonlinear Langevin dynamics and the Fokker–Planck equation, which are used to describe the stochastic evolution of income.

### Equation 1: Nonlinear Langevin Equation

$$
\frac{dm}{dt} = -A(m) + C(m) \eta(t)
$$

---

## Yakovenko et al. Model

- **Low-Income Class:** Applies the Boltzmann–Gibbs law, which predicts an exponential distribution.

- **Medium-Income Class:** Applies the weak Pareto law, describing a power-law distribution.

### Equation 2: Complementary Cumulative Distribution Function

$$
\Pi(m) = \int_{m}^{\infty} P_{eq}(m') dm' = \exp \left( - \frac{m - m_{init}}{T} \right)
$$

---

## Our Extension

- **Inclusion of High-Income Class:** The study extends the model to describe high-income class distributions.

- **Unified Formula:** The extended model provides a unified formula covering low, medium, and high-income classes.

### Equation 3: Unified Formula for Income Distribution

$$
P_{eq}(m) = 

\begin{cases}

c' \cdot \frac{\exp \left( -\left( \frac{m_{0}}{T} \right) \arctan \left( \frac{m}{m_{0}} \right) \right)}{[1 + \left( \frac{m}{m_{0}} \right)^{2}]^{(\alpha + 1)/2}}, & \text{if } m < m_{1} \ 

c'' \cdot \frac{\exp \left( -\left( \frac{m_{0}}{T_{1}} \right) \arctan \left( \frac{m}{m_{0}} \right) \right)}{[1 + \left( \frac{m}{m_{0}} \right)^{2}]^{(\alpha_{1} + 1)/2}}, & \text{if } m \ge m_{1}

\end{cases}
$$

---

## Threshold Formulas

- **Crossover Points:** The model introduces crossover points \(m_{0}\) and \(m_{1}\) to distinguish between different income classes.

- **Threshold Forms:** The drift and diffusion coefficients \(A(m)\) and \(B(m)\) are defined differently above and below these thresholds.

### Equation 4: Threshold Forms for \(A(m)\) and \(B(m)\)

$$
A(m) = 

\begin{cases} 

A^{<}(m) = A_{0} + am, & \text{if } m < m_{1} \ 

A^{\ge}(m) = A_{0}' + a'm, & \text{if } m \ge m_{1} 

\end{cases}
$$

$$
B(m) = 

\begin{cases} 

B^{<}(m) = B_{0} + bm^{2} = b (m_{0}^{2} + m^{2}), & \text{if } m < m_{1} \ 

B^{\ge}(m) = B_{0}' + b'm^{2} = b'(m_{0}'^{2} + m^{2}), & \text{if } m \ge m_{1} 

\end{cases}
$$

---

## Results

- **Theoretical vs. Empirical:** The model's predictions are compared with empirical data from 2006 and 2008, showing a good fit.

- **Validation:** The model successfully describes income distribution across all classes, validating its applicability.

### Figure 1: Model Fit to Empirical Data

---

## Discussion

- **Model Accuracy:** The model accurately captures the income distribution, including the existence of a third income region.

- **Class Characteristics:** 

  - Low-income class: Exponential distribution.

  - Medium-income class: Weak Pareto law.

  - High-income class: Zipf's law.

---

## Conclusions

- **Extended Model:** The model successfully describes EU household incomes.

- **Economic Insights:** High-income class activities are riskier; the medium-income class's role is reduced.

- **Future Work:** Apply the model globally and validate with comprehensive data.

---

## Acknowledgments

- Acknowledge contributors and data sources.

- Recognize foundational work by previous researchers.

---

## Questions

- Open the floor for questions and further discussion.
