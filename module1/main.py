md_content = """
# Analysis of Labor Strike Based on Evolutionary Game and Catastrophe Theory

## Authors:
- Ahmad Makui
- Seyed Mohammad Seyedhosseini
- Seyed Jafar Sadjadi
- Parinaz Esmaeili

## Abstract
This paper analyzes the labor-employer relations during conditions that lead to strike using an evolutionary game and catastrophe theory. During a threat to strike, the employers may accept the whole or only a part of the demands of labors and improve the work conditions or decline the demands, and each selected strategy has its respective costs and benefits. The threat to strike action causes the formation of a game between the strikers and employers that, as time goes on, different strategies are evaluated by the players and the effective variables of strike faced gradual and continuous changes, which can lead to a sudden jump of the variables and push the system to very different conditions such as dramatic increase or decrease in the probability of selecting strategies. So the alliance between labors could suffer or reinforce. This discrete sudden change is called catastrophe. In this study, after finding evolutionary stable strategies for each player, the catastrophe threshold analyzed by nonlinear evolutionary game and the managerial insight is proposed to employers to prevent the parameters from crossing the border of the catastrophe set that leads to a general strike.

## Introduction
Strike is a temporary work stoppage caused by workers to achieve their goals and demands. Various reasons like pay raise, reducing working hours, and so on lead to strikes. This study focuses on the evolutionary game models of labor-employer relations during the strike.

## Model and Assumptions
Each strategy chosen by labors or employers during strike causes costs and benefits. The strategies are shown in the following table:

| Labors                  | Employers Improve (Cooperation) | Employers Not Improve (Defection) |
|-------------------------|---------------------------------|-----------------------------------|
| Strike (Defection)      | (Bl - Cl - Ce - Be)             | (-Cl - Al - Ce)                   |
| Not Strike (Cooperation)| (Bl - Be)                       | (0,0)                             |

The relevant variables are defined in the following table:

| Variables | Definitions                           |
|-----------|---------------------------------------|
| Cl        | Cost of "strike" for labors           |
| Bl        | Benefit of "improve" for labors       |
| Al        | Cost of "losing credit" for labors    |
| Ce        | Cost of "production stoppage" for the employers |
| Be        | Cost of "improve" for the employers   |

## Equilibrium Analyses
At the primary stage, we assume that the probability that the labors choose the "strike" strategy (defection) is $x$, and the probability that the employers choose the "improve" strategy (cooperation) is $y$. The respective expectation values of "strike" and "not strike" for labors are $U_{1Y}$ and $U_{1N}$ and labors’ average value is $\overline{U_1}$, then,

$$
U_{1Y} = y(B_l - C_l) + (1 - y)(-C_l - A_l) = yB_l - C_l - A_l + yA_l
$$

$$
U_{1N} = yB_l
$$

$$
\overline{U_1} = x(yB_l - C_l - A_l + yA_l) + (1 - x)(yB_l) = -x(C_l + A_l) + y(xA_l + B_l)
$$

The respective expectation values of "improve", "not improve" and the employer’s average value are $U_{2Y}$, $U_{2N}$ and $\overline{U_2}$:

$$
U_{2Y} = x(-C_e - B_e) + (1 - x)(-B_e) = -xC_e - B_e
$$

$$
U_{2N} = -xC_e
$$

$$
\overline{U_2} = y(-xC_e - B_e) + (1 - y)(-xC_e) = -yB_e - xC_e
$$

### Replicator Dynamics Equation of "Strike" Labor Population
The replicator dynamics equation is:

$$
F(x) = \frac{dx}{dt} = x \left( U_{1Y} - \overline{U_1} \right) = x (x - 1) (A_l - yA_l + C_l)
$$

### Replicator Dynamics Equation of "Improve" Employer Population
The replicator dynamics equation is:

$$
F(y) = \frac{dy}{dt} = y \left( U_{2Y} - \overline{U_2} \right) = y (y - 1) B_e
$$

## Background of Catastrophe Theory
Catastrophe theory was proposed by René Thom in the 1960s. It defines that small changes in certain parameters of a nonlinear system can cause equilibrium to appear or disappear leading to large and sudden changes in the behavior of the system.

The equation of the classic catastrophe theory is:

$$
\frac{dx(t)}{dt} = - \frac{\partial V ( x(t), \bar{c} )}{\partial x(t)}
$$

### The Existence of the Catastrophe for the Labor Population
The replicator dynamics equation for the labor population is presented below. It is assumed that $P(\text{improve}) = z \cdot P(\text{strike})$.

$$
\frac{dx(t)}{dt} = x(t) \left( U_x - \overline{U} \right) dt = x (x - 1) (A_l - zxA_l + C_l) dt
$$

Expanding the equation:

$$
\frac{dx(t)}{dt} = \left( x^3(-zA_l) + x^2(zA_l + A_l + C_l) + x(-A_l - C_l) \right) dt = (Ax^3 + Bx^2 + Cx) dt
$$

$$
A = -zA_l \quad B = zA_l + A_l + C_l \quad C = -A_l - C_l
$$

Assuming $\alpha, \beta$ and $Z$:

$$
x = Z - \frac{B}{3A}, \quad \alpha = \left( C - \frac{B^2}{3A^2} \right), \quad \beta = \left( \frac{2}{27} \frac{B^3}{A^3} - \frac{1}{3} \frac{CB}{A^2} \right)
$$

$$
\frac{dx(t)}{dt} = A (Z^3 + \alpha Z + \beta) dt \rightarrow \frac{dx(t)}{dt} = 0 \rightarrow Z^3 + \alpha Z + \beta = 0
$$

## Conclusion
The study of the evolutionary game model of labors strike due to inappropriate work conditions is presented. Equilibrium analysis through the replicator dynamics equations showed that the final choices for labors and employers are strike and not improve, respectively. The possibility of catastrophe occurrence in the labor population is proved using catastrophe theory.
"""

with open("analysis_of_labor_strike.md", "w") as file:
    file.write(md_content)

md_content
