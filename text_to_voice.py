from gtts import gTTS
import os

mytext = """
### Abstract

Herein, we applied statistical physics to study incomes of three (low-, medium- and high-income) society classes instead of the two (low- and medium-income) classes studied so far. In the frame of the threshold nonlinear Langevin dynamics and its threshold Fokker–Planck counterpart, we derived a unified formula for the description of income of all society classes, by way of example, of those of the European Union in years 2006 and 2008. Hence, the formula is more general than the well-known formula of Yakovenko et al. That is, our formula well describes not only two regions but simultaneously the third region in the plot of the complementary cumulative distribution function vs. an annual household income. Furthermore, the known stylized facts concerning this income are well described by our formula. Namely, the formula provides the Boltzmann–Gibbs income distribution function for the low-income society class and the weak Pareto law for the medium-income society class, as expected. Importantly, it predicts (to satisfactory approximation) the Zipf law for the high-income society class. Moreover, the region of medium-income society class is now distinctly reduced because the bottom of the high-income society class is distinctly lowered. This reduction made, in fact, the medium-income society class an intermediate-income society class.

### 1. Introduction

For over two decades, physics-oriented approaches have widely been developed to explain different economic processes. Those approaches aim at formulating well-fitted unbiased indicators of social and economic phenomena. One of their key issues is the income of society analysis using methods of statistical physics. The main goal of this economic issue is to unravel and describe mechanisms of societies’ enrichment or impoverishment.

The first successful attempt in this socio-economic field was made by the legendary economist and sociologist Vilfredo Pareto. He demonstrated that the distribution functions of individual incomes in different countries within a stable economy are universal being manifested by a power law. This law is called the weak Pareto law. He emphasized that this law could not resemble the distribution functions obtained if the gain and accumulation of income were random. As a possible origin of this law, Pareto indicated a self-similarity structure of societies.

Pareto’s economic discoveries initiated attempts of analytical descriptions of incomes of the societies and inspired an avalanche of related research works. Among them, particularly significant are those of the economist Robert Gibrat. He found that the complementary cumulative distribution function of the Pareto distribution is insufficient to describe empirical data within the whole range of the income. Trying to find a functional form that could account for these data, he proposed a rule called the Rule of Proportionate Growth.

Furthermore, the income of societies was analyzed by David Champernowne, who constructed a stochastic model simulating the Pareto power law and also by Benoit Mandelbrot who described several useful properties of random variables subject to the Pareto distribution.

In the recent decade, a large number of studies were performed aiming at the construction of models, which (to some extent) would well replicate the observed complementary cumulative distribution functions of individual incomes. Among them, the most significant seems to be the Clementi–Matteo–Gallegati–Kaniadakis approach, the Generalized Lotka–Volterra Model, the Boltzmann–Gibbs law, and the Yakovenko et al. model. Very recently, a mathematical model similar to that of Yakovenko et al. has been developed. It involves complex economic justification for microscopic stochastic dynamics of wealth. However, none of the above attempts to find an analytical description of the income structure solves the principal challenges, which concern:

(i) the description of the annual household incomes of all society classes (i.e. the low-, medium-, and high-income society classes) by a single unified formula and (ii) the problem regarding corresponding complete microscopic (microeconomic) mechanism responsible for the income structure and dynamics.

In our considerations presented herein, we used Boltzmann–Gibbs law and Yakovenko et al. model to derive a uniform analytical formula describing income of all three society classes.

### 2. Extended Yakovenko et al. model

In accord with an effort outlined above, we compared the empirical data of the annual household incomes in the European Union (EU), including Norway and Iceland, with predictions of our theoretical approach proposed herein. This approach is directly inspired by the Yakovenko et al. model. By using the same assumptions, however, we generalized this model to solve the principal challenges (i) and (ii) indicated above.

We used data records from the Eurostat Survey on Income and Living Conditions (EU-SILC) by way of example for years 2006 and 2008 (containing around 150 and 200 thousand empirical data points, respectively). However, these records do contain (as all other records) only a few data points concerning the high-income society class, i.e. the third region in the plot of the complementary cumulative probability distribution function vs. annual household income. To consider this region, we made an extension of these empirical data by adding the data points of billionaires’ incomes (i.e. the income greater than around 10^9 euros) taken from the Forbes list. Here, for consistency, we changed the term ‘multimillionaire’ used in the European terminology into the US dollar term billionaire. We recalculated US dollars to euros by using the mean exchange rate at the day of construction of the Forbes ‘The World’s Billionaires’ rank.

We were able to correct incomes of three society classes thanks to the following procedure.

(i) Firstly, we selected EU billionaires’ wealth from the Forbes ‘The World’s Billionaires’ rank, for instance, for four successive years 2005–2008. (ii) Secondly, we calculated the corresponding differences between billionaires’ wealth for the successive years. We assumed that their incomes are, in fact, proportional to these differences. For instance, we calculated the billionaire incomes for the year 2006 by taking the difference between their wealth in years 2006 and 2005. We made it analogously for the year 2008. However, we took into account only billionaires who gained effective incomes (neglecting those, who suffered from income losses). (iii) Subsequently, having so calculated incomes for the high-income society class, we joined them (separately for years 2006 and 2008) with the corresponding EU-SILC datasets. By using so completed datasets, we then constructed the initial empirical complementary cumulative distribution function for years 2006 and 2008. For that, we used the well-known Weibull recipe. However, this direct approach shows a wide gap of incomes inside the high-income society class resulting in a horizontal line of the complementary cumulative distribution function. To fill in the gap separates the first segment belonging to the high-income society class, consisting of all data points taken from the EU-SILC dataset (only 8 for 2006 and 6 for 2008), from the second segment, consisting of remaining data points (76 for 2006 and 96 for 2008), which also belong to the high-income society class but are taken from the Forbes dataset. (iv) In the final step, we eliminated this gap by adopting the assumption that the empirical complementary cumulative distribution functions (concerning the whole society) have no unnatural segments. That is, we assumed that statistics of incomes is a continuous function of income. Hence, we were forced to multiply the billionaire incomes from Forbes dataset by the properly chosen common proportionality factor. This factor was equal to 1.0×10^−2 for both years, as we assumed the requirement of full overlap of the first (above mentioned) segment by the second segment. This assumption leads to a unique solution (up to some negligible statistical error) for this proportionality factor. We found that this factor was only a slowly-varying function of time (or years).

Hence, we received the data record containing already a sufficient number of data points for all society classes, including the high-income society class. Although the Forbes empirical data only roughly estimate the wealth of billionaires, they quite well establish the billionaires’ rank, thus sufficiently justifying our approach. This is because our purpose is to classify billionaires to concrete universality class rather than finding their total incomes. Our procedure of linking data from two different bases does not violate this universality class.

The basic tool of our analysis is an empirical complementary cumulative distribution function being typical in this context. We calculated it according to the standard two-step procedure. For that, first, the income empirical data were ordered according to their rank, i.e., from incomes of the richest households to those of the poorest. Next, in accordance with the well-known Weibull formula, we calculated the ratio \\( \\frac{l}{N+1} \\) where \\( l \\) is the position of the household in the rank and \\( N \\) is the size of the empirical data record. This ratio directly determines the required fraction of households of the income higher than that related to a given household position \\( l \\) in the rank. The complementary cumulative distribution function obtained that way is sufficiently stable. Furthermore, it does not reduce the size of the output compared to that of the original empirical data record.

### 2.1. Hint to the Yakovenko et al. model

Let \\( m \\) be an influx of income per unit time to a given household. We treat \\( m \\) as a variable obeying stochastic dynamics. Then, we can describe its time evolution by using the nonlinear Langevin equation.

Here, \\( A(m) \\) is a drift term and \\( \\eta(t) \\) is a white noise, where the coefficient \\( C(m) \\) is its \\( m \\)-dependent amplitude. As we prove below, already white noise is herein sufficient to produce two different power-laws. Obviously, generalization with respect to power-law noise is also possible and

 very promising. Noteworthy, jump effects are important in the financial and social phenomena because they naturally produce power-law tails. However, correspondence between Itô and Stratonovich representations is then no longer trivial.

Notably, the above nonlinear stochastic dynamics equation is equivalent to the following Fokker–Planck (continuity) equation for the probability distribution function.

The equilibrium solution of Eq. (2), \\( P_{eq} \\), defined by vanishing of \\( J(m,t) \\), takes the form:

Following the Yakovenko et al. model, we can assume that changes of income of the low-income society class are independent of the previous income gained. This assumption is justified because the income of households belonging to this class mainly takes the form of wages and salaries. The stochastic process associated with the mechanism of this kind is called the additive stochastic process. In this case, coefficients \\( A(m) \\) and \\( B(m) \\) take, obviously, the form of positive constants.

This choice of coefficients leads to the Boltzmann–Gibbs law with the exponential complementary cumulative distribution function.

In Eq. (6), the distribution function is characterized by a single parameter, i.e. an income temperature \\( T \\), which can be interpreted in this case as an average income per household.

For the medium- and high-income society classes, we can assume (again following Yakovenko et al.) that changes of income are proportional to the income gained so far. This assumption is also justified because profits go to the medium- and high-income society classes mainly through investments and capital gains. This type of stochastic process is called the multiplicative stochastic process. Hence, coefficients \\( A(m) \\) and \\( B(m) \\) obey the proportionality principle of Gibrat.

By using the equilibrium distribution function, Eq. (4), we arrive in this case to the weak Pareto law with the complementary cumulative distribution function.

Here, \\( m_{sp} \\) is a scaling factor (depending on \\( a \\), \\( b \\), and \\text{const}) while \\( \\alpha = 1 + \\frac{a}{b} \\) is the Pareto exponent. The ratio of the \\( a \\) to \\( b \\) parameters can directly be determined from the empirical data expressed in the log–log plot (by using their slopes).

As Yakovenko et al. have already found, the coexistence of additive and multiplicative stochastic processes is allowed. By assuming that these processes are uncorrelated, we get.

This consideration leads (together with Eq. (4)) to a significant Yakovenko et al. model with the probability distribution function given by:

where parameters \\( \\alpha \\) and \\( T \\) are defined above. For \\( m \\ll m_0 \\), Eq. (10) becomes the Boltzmann–Gibbs law while for \\( m \\gg m_0 \\) it becomes the weak Pareto law. Notably, the \\( m_0 \\) parameter is the crossover income between ranges of additive and multiplicative processes.

### 2.2. Our extension

Based on the Yakovenko et al. model, the complementary cumulative distribution function can be used to describe income of only low- and medium-income society classes. However, it does not capture that of the most intriguing high-income society class. Therefore, the goal of our present work is to derive from Eq. (4) such a distribution function, which would cover all three ranges of the empirical data records, i.e. low-, medium-, and high-income classes of the society (including also without intermediate regions between them).

The high-income society class is mainly composed of the company owners. Hence, besides the weak Pareto law, we expect (to a good approximation) the Zipf law (the Zipf law is the Pareto law with the exponent \\( \\alpha = 1 \\)). In order to derive the Zipf law from Eq. (4), we have to provide, therefore, functions \\( A(m) \\) and \\( B(m) \\) in the threshold form.

where \\( m_0^2 = \\frac{B_0}{b} \\) and \\( m_0'^2 = \\frac{B_0'}{b'} \\). The threshold parameter \\( m_1 \\) can be interpreted as a crossover income between the medium- and high-income society classes. Remarkably, both income crossovers \\( m_0 \\) and \\( m_1 (\\ge m_0) \\) are exogenous parameters. They should be determined from the dependence of the empirical complementary cumulative distribution function on variable \\( m \\) because both crossovers are sufficiently distinct.

Apparently, we assumed above that the formalism of the income change is the same for the whole society. This formalism is expressed by the threshold nonlinear Langevin equation where particular dynamics distinguishes the range of the high-income society class from those of the others.

For protection of the equilibrium distribution function against discontinuity at the threshold \\( m_1 \\) (which means adoption of the continuity principle of the equilibrium distribution function of household incomes being a kind of Ockham's razor principle), the following requirement should be satisfied.

By substituting Eqs. (14) and (15) into Eq. (13), we directly obtain.

To assure that the reinterpretation of the parameter \\( m_0' \\) is consistent with the income crossover \\( m_0 \\), we further put.

Subsequently, by substituting Eqs. (11) and (12) into Eqs. (14) and (15), we finally get.

where \\( \\alpha_1 = 1 + \\frac{a'}{b} \\) and \\( T_1 = \\frac{B_0}{A_0'} \\) while \\( c' \\) and \\( c'' \\) are mutually related constants. These constants are proportional to the normalization factor const. Besides, constant \\( c' \\) depends on \\( m_{init} \\), \\( m_0 \\), \\( T \\), and \\( \\alpha \\) while \\( c'' \\) additionally depends on \\( T_1 \\), \\( m_1 \\), and \\( \\alpha_1 \\). Apparently, the number of free (effective) parameters driving the two-branch distribution function, Eq. (19), is reduced because this function depends only on the ratio of the initial parameters defining the Langevin dynamics.

For \\( m \\gg m_0 \\), the integration of the distribution function, Eq. (19), is self-consistent, as required, because the two power-law regimes are well defined. Then, for instance for \\( m \\gg m_0 \\), the second branch in Eq. (19) becomes the power-law dependence driven by the Pareto exponent \\( \\alpha_1 \\) different (in general) from \\( \\alpha \\).

Importantly, our analysis indicates that the existence of the third income region is already allowed by theory. We are following this indication below.

### 3. Results and discussion

In principle, we are ready to compare the theoretical complementary cumulative distribution function based on our probability distribution function \\( P_{eq}(m) \\), given by Eq. (19), with the empirical data for the whole income range. However, the analytical form of this theoretical complementary cumulative distribution function is unknown in the closed explicit form. Therefore, we calculate it numerically. The key technical question arises on how to fit this complicated theoretical function to the empirical data. The fitting procedure consists of three steps as, fortunately, all parameters are to be found (in principle) by using independent fitting procedures, as follows.

In the initial step, we found numerically (more or less) approximated values of crossovers \\( m_0 \\) and \\( m_1 \\) directly from the plot of the empirical complementary cumulative distribution function (or empirical data). Thus, the uncertainty of the \\( m_0 \\) and \\( m_1 \\) parameters did not exceed 10%%, which was sufficiently accurate. Moreover, we took the exact value of the parameter \\( m_{init} \\) as the first point in the record of the empirical data.

Secondly, we determined the temperature \\( T \\) value by fitting the Boltzmann–Gibbs formula, Eq. (6), to the corresponding empirical data in the range extending from \\( m_{init} \\) to \\( m_0 \\) (both found in the initial step). Notably, we assumed that this formula could be characterized by a single temperature value since the society as a whole was considered to be in (partial) equilibrium during the whole fiscal year. That is, we further put \\( T_1 = T \\Rightarrow A_0' = A_0 \\).

At the third step, we determined exponents \\( \\alpha \\) and \\( \\alpha_1 \\) by separately fitting the weak Pareto law to the empirical data for the medium- and high-income society classes, respectively.

The results obtained in these three steps are correspondingly presented in Figures 1 and 2, mainly in the log–log scale (only in Figure 1 the inserted plot is presented in the log–linear scale).

The plot in Figure 1 shows the complementary cumulative exponential distribution function, i.e. the Boltzmann–Gibbs law, Eq. (6), which quite well describes the EU low-income society class. This finding significantly supports universal applicability of the Boltzmann–Gibbs law in the economy.

Subsequently, the plot in Figure 2 was constructed. It quite well describes the EU medium-income society class by the weak Pareto law. Apparently, by joining the Forbes empirical database concerning an effective income of billionaires with the EU-SILC database, we found that the Pareto (effective, non-universal) exponent increased from \\( \\alpha = 2.28 \\pm 0.01 \\) to \\( \\

alpha = 2.902 \\pm 0.002 \\). This result defines the range of Pareto exponents. This range covers, e.g. the exponent \\( \\alpha = 2.67 \\) obtained very recently for the medium-income society class in Romania for 2008 by considering a voluminous social security database. However, this database contains only empirical data for low- and medium-income society class (in our terminology). In principle, it would also be possible to join this voluminous database with the Forbes corresponding dataset if Romanian billionaires are present as members of the Forbes rank. As a result of our joining, the range of the medium-income class becomes much narrower and shifted to income increased by one order of magnitude. The medium-income society class is so sensitive to the size of the high-income society class as the former contains only no more than 3%% of all households.

These results are significant as they demonstrate the crucial importance of the two-income society classes in the society structure, that is the low- and the high-income society classes.

### 4. Conclusions

Herein, we proved that the household incomes of all society classes in the EU can be modeled by the nonlinear threshold Langevin dynamics with \\( m \\)-dependent drift term, \\( A(m) \\), and \\( m \\)-dependent dispersion, \\( B(m) \\), given by Eqs. (11) and (12), respectively. At the threshold \\( m_1 \\), there is a jump of the proportionality coefficient of the drift term. That is, this term abruptly changes from \\( a \\) to \\( a' \\), where \\( a' < a (\\alpha_1 < \\alpha) \\). It means that the stochastic term in Eq. (1) is relatively more significant in this case (i.e. above the threshold \\( m_1 \\)) than the drift term. That is, the economic activity of the high-income society class is much riskier than the activities of all other society classes, as expected.

By comparing results obtained for years 2006 and 2008 (cf. Figures 4 and 5), we found that the threshold \\( m_1 \\) was only slightly higher for the latter year than for the former. It means that in the year 2006, to the high-income society class belonged the society members almost as rich as those belonging to this class in the year 2008. Moreover, the result of only slightly more extensive society stratification in the year 2008 was confirmed by exponents' inequality, as the exponent \\( \\alpha_1 \\) for the year 2006 is only slightly higher than that for the year 2008. Furthermore, the slowly-varying tendency (similar to that considered above) is also observed for the medium-income society class. In fact, it is surprisingly stable with respect to the fractional effect that crisis the shape of the curve \\( \\Pi(m) \\) vs. \\( m \\). That is, only the number of households belonging to a given income society class most likely changed but the income structure of the society as a whole was not altered.

The completed database, which we used (by properly joining the Forbes empirical database with that of EU-SILC), emphasizes a significant role of the high-income society class. Namely, the presence of the third region increases this Pareto exponent which characterizes the medium-income society class making the range of this class narrower and shifting it to incomes lower by one order of magnitude (cf. Figure 2). This latter society class is now so much reduced that it occupies almost an intermediate region between low- and high-income society classes. Apparently, the role of the low- and medium-income society classes was, in the present case, significantly reduced.

The use of two different datasets (EU-SILC and Forbes), which are not necessarily compatible, carries a methodological danger of getting discontinuous fits. Nevertheless, bringing these two datasets together and analyzing them jointly is better for making progress in this field than avoiding their comparison.

Herein, we succeeded in comparing ratios (i.e. relative population of successive income society classes) of \\( r_1 = \\frac{P_{eq}(m_{init}) - P_{eq}(m_0)}{P_{eq}(m_{init}) - P_{eq}(m_1)} \\) and \\( r_2 = \\frac{P_{eq}(m_{init}) - P_{eq}(m_1)}{P_{eq}(m_{init})} \\) for both years 2006 and 2008 by using our formula, Eq. (19). Hence, we determined \\( r_1 = 32.66 \\) and \\( r_2 = 16.48 \\) for the year 2006 as well as \\( r_1 = 48.98 \\) and \\( r_2 = 13.97 \\) for the year 2008. We obtained information on, relatively, how many society members belong to a given income society class. Apparently, the population of the medium-income society class is strongly decreased in the year 2008 in comparison to that in the year 2006. Several members of this class were shifted both to the low- and to high-income society classes. Our two-parameter approach seems to be much more sensitive than that using the Gini coefficient (G) because we obtained \\( G = 54.34 \\) and \\( G = 54.89 \\) for the years 2006 and 2008, respectively.

Furthermore, we estimated the percentage breakdown of the population of the society classes: for the year 2006—low-income: 96.85%%; medium-income: 2.97%%; high-income: 0.18%% and for the year 2008—low-income: 97.86%%; medium-income: 2.00%%; high-income: 0.14%%. These results can be considered as complementary to that (obtained above) corresponding to the relative population of successive income society classes. Interestingly, the total fraction of the medium- and high-income classes in the EU was around 3%% in 2006, which is about the same as that found by Yakovenko et al. for the US, and this fraction has decreased to around 2%% in the year 2008, most likely due to the financial crisis.

Economists agree that macroeconomic and political conditions are quite different in the US and in the EU, and expect a different lower income inequality in the EU. However, we demonstrate quantitatively herein that the exponential law does apply to the EU as well. This finding gives much stronger support for universal applicability of the Boltzmann–Gibbs law in economics.

Our work shows that the income distribution in the low-income class, covering around 97%% of the population, follows the exponential law, whereas in the two upper-income classes the distribution follows two power laws with different exponents. Remarkably, the role of the medium-income society class is strongly reduced making it an intermediate one within our approach to the complementary cumulative distribution function.

We hope that our results will be useful for studies of static and dynamic properties of the household incomes not only for the EU as a whole but also for those of other continents and countries, if only sufficiently honest, large, and complete (i.e. covering all society classes) empirical data are available.
"""

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")