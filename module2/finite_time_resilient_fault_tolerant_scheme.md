# Finite-Time Resilient Fault-Tolerant Investment Policy Scheme for Chaotic Nonlinear Finance System

## 1. Introduction

### 1.1 Background and Motivation
- Chaotic systems are essential for modeling various real-world problems in science, economics, finance, and engineering.
- These systems exhibit sensitive dependence on initial conditions, making their behavior unpredictable and challenging to control.
- The chaotic nonlinear finance system models economic factors like economy policy, share loss, and natural disasters.

## 2. Problem Formulation
- The state variables of the nonlinear chaotic finance system are investment $ x_2 $, price index $ x_3 $, and the interest rate $ x_1 $.
- The system is described by:
$$
\begin{aligned}
    \dot{x}_1(t) &= x_3(t) + (x_2(t) - p)x_1(t), \\
    \dot{x}_2(t) &= 1-q x_2(t) - x_1^2(t), \\
    \dot{x}_3(t) &= -r x_3(t) - x_1(t)
\end{aligned}
$$
- Where $ p $, $ q $, and $ r $ are positive parameters.
- The control system can be represented as:
$$
\dot{x}(t) = A x(t) + u(t) + C w(t) + f(x(t)),
$$
where:
$$
A = \begin{bmatrix}
-p & 0 & 1 \\
0 & -q & 0 \\
-1 & 0 & -r
\end{bmatrix}, \quad
f(x(t)) = \begin{bmatrix}
x_1 x_2 \\
1-x_1^2 \\
0
\end{bmatrix}.
$$

## 3. Main Contributions
- Development of a resilient fault-tolerant guaranteed cost controller with delay to manage fluctuations in investment policy.
- The controller aims to achieve finite-time boundedness with minimum guaranteed cost.
- Theoretical results validated by MATLAB LMI toolbox and numerical simulations.

## 4. Theoretical Results

### Theorem 1: Control System Stability
$$
\Pi = \begin{bmatrix}
\Pi_{11} & X_1 G K_2 & 0 & X_5 & X_1 C & X_1 & L \\
& (1 - \mu) X_2 & 0 & -X_5 & 0 & 0 & 0\\
& * & -X_3 & 0 & 0 & 0 & 0\\
& * & * & -X_4 & 0 & 0 & 0 \\
& * & * & * & -\alpha I & 0 & 0 \\
& * & * & * & * & -I & 0 \\
& * & * & * & * & * & -I
\end{bmatrix} < 0,
$$
where:
$$
\Pi_{11} = A^T X_1 + X_1 A + X_1 K_1 G K_1 + K_1 G^T X_1 + X_2 + X_3 + \tau^2 X_4 - \alpha X_1.
$$

### Theorem 2: Robust Finite-Time Boundedness
- **Theorem 2:** For given constants and symmetric matrix $ R $, the closed-loop system is robustly finite-time bounded with a disturbance attenuation level $ \gamma $:
$$
\begin{aligned}
    [\tilde{\Pi}_{i,j}] &< 0, \\
    \sigma R^{-1} &< X < R^{-1}, \\
    0 < X_2 &< 2R^{-1}, \\
    0 < X_3 &< 2R^{-1}, \\
    0 < X_4 &< 2R^{-1}, \\
    0 < X_5 &< 2R^{-1},
\end{aligned}
\\
\begin{aligned}
    c_a + [d - (d + c_b) e^{-\alpha} \sqrt{(4\tau + \tau^3 + 2 \tau^2)c_a}] &< 0.
\end{aligned}
$$

### Theorem 3: Guaranteed Cost Controller
- **Theorem 3:** Provides conditions for the existence of a guaranteed cost controller with minimum cost bound $ \bar{J} $:
$$
\tilde{\Pi}_{i,j} < 0, \quad \forall i, j \in \mathbb{R},
$$
- The finite-time guaranteed cost bound is:
$$
\bar{J} = e^{\alpha N} \lambda_2 + \tau (\lambda_3 + \lambda_4) + \frac{\tau^3}{2} \lambda_5 + \tau^2 \lambda_6 c_a.
$$

## 5. Numerical Simulations
- Parameters: $ p = 2.1 $, $ q = 3 $, $ r = 1 $, and the capital inflow risk matrix $ G $ is considered as $ 0.6I $.
- Initial values: $ [0.3, 0.3, 0.4] $.
- State trajectories and control responses demonstrate the effectiveness and robustness of the designed controller.
- The controller ensures convergence to desired equilibrium points within finite-time bounds even in the presence of faults.
- Parameters used in simulations:
$$
\begin{aligned}
    \tau &= 1.3, \\
    f &= 6.6260, \\
    K_1 &= \begin{bmatrix}
    -174.1836 & -25.4263 & -37.8756 \\
    -25.4263 & -217.2244 & -76.8075 \\
    -37.8756 & -76.8075 & -281.6521
    \end{bmatrix}, \\
    K_2 &= \begin{bmatrix}
    0.5383 & 0.0035 & -0.0259 \\
    0.0035 & 0.5621 & 0.0025 \\
    -0.0259 & 0.0025 & 0.3914
    \end{bmatrix}.
\end{aligned}
$$

## 6. Conclusion
- A finite-time resilient fault-tolerant guaranteed cost investment policy scheme for the chaotic nonlinear finance system is developed.
- The approach effectively manages unpredictable changes and fluctuations in the finance system, achieving minimum cost and stability.
- Simulation results reveal the efficacy of the proposed scheme, ensuring robust performance over a finite period.
