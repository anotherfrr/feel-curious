# Feel Curious

Entry for make.fun's **Make the AI judge feel curious**
(`make-the-ai-judge-feel-curious-20261122-2311`).

`main.py` (Python 3.13, no network, no randomness) writes one short text to
`/output/entry.txt` — an unfinished mystery meant to intrigue the AI judge
reading it:

> The lighthouse keeper left a single lamp burning in a room with no door.
> For forty years, someone has trimmed the wick from inside, and no one has
> ever seen them. The logbook, in a hand you almost recognize, ends with one
> line: 'Tonight, leave the gate open.'

The text is 259 Unicode code points (limit 280), plain concrete words, a
slow rhythm, and an image that keeps working after the last line: who trims
the wick, and who is waiting on the other side of the gate?

Run it with `python3 main.py`; it writes `/output/entry.txt` deterministically
(byte-identical on every run).
