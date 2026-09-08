# Huffman Coding for a Markov-Chain (Memory) Binary Source

Implementation and analysis of Huffman coding applied to a first-order Markov binary source, with entropy computed at increasing block lengths (1, 2, 3 symbols) to show how source extension improves compression efficiency.

## What it does

- Generates a random binary sequence (N = 1000) from a first-order Markov source, defined by transition probabilities `P(0|0)` and `P(1|1)`
- Computes the source entropy `H1` from the stationary and joint probabilities
- Groups the sequence into blocks of 2 and 3 symbols and computes the extended-source entropies `H2` and `H3`
- Builds a Huffman code at each block level and measures the resulting compressed length (`L1`, `L2`, `L3`)

## Run it

```bash
python main.py
```

You'll be prompted for the two conditional probabilities:

```
Unesite verovatnocu da se posle 0 javi 0: 0.9
Unesite verovatnocu da se posle 1 javi 1: 0.9
```

## Example output

```
Entropija: 0.4690 [Sh/simb]

======= Hafmanov kod =======
L1: 1000
H2: 0.6779 [Sh/simb]
L2: 777
H3: 0.6122 [Sh/simb]
L3: 639
```

## Key result

As block length increases (1 → 2 → 3 symbols), the block entropy `Hk` converges toward the true source entropy, and the Huffman-compressed length drops accordingly — Huffman coding exploits the statistical dependence between consecutive symbols more effectively at higher block orders.

As a control case, when `P(0|0) = P(1|1) = 0.5` the source becomes memoryless (i.i.d.), and compression gives no improvement at any block order (`L1 ≈ L2 ≈ L3`) — matching the theoretical expectation that Huffman coding can't compress a source with no statistical structure.

## Report

Full derivation of the entropy formulas and theoretical background: [`report/OTR_domaci.pdf`](report/OTR_domaci.pdf) (in Serbian).
