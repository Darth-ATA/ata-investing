# Oscillators

## Stochastic Oscillator

The Stochastic Oscillator could be interpreted as a indicator of buy/sell signals.
Is composed by *K* and *D* lines but usually we use *SK* and *SK* that are softener versions of *K* and *D*:

$$
\begin{aligned}
    K &= \frac{Lc - min(pp)}{max(pp) - min(pp)} * 100,\ K \in [0, 100]\\
    D &= mean(k, n),\ D \in [0, 100] \\
    where: \\
    n &= \mathrm{number\ of\ periods.\ I\ will\ use\ } n=6 \\
    Lc &= \mathrm{last\ closing\ price} \\
    pp &= \mathrm{period\ closing\ prices} \\
    mean(x, m) &= \mathrm{mean\ of\ the\ last\ m\ of\ x\ values} \\ \\
    SK &= D \\
    SD &= mean(SK, n) \\
    SK & \in [0, 100] \\
    SD & \in [0, 100]
\end{aligned}
$$

The cut between *SK* and *SD* is the buy/sell signal. It could mean an end of a trend or a change in the trend.

In a bull market, the buy signal is when *SK* cuts *SD* in the up direction. Is more accurate for buying than for selling
In a bear market, the sell signal is when *SK* cuts *SD* in the down direction. Is more accurate for selling than for buying.

Is more accurate when cuts are produced in the overbought/oversold zones.

Where is more accurate is in lateral trends.

Also can predict a change in the trend checking diveregences between the price and the oscillator.
