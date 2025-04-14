#### Prisoner's Dilemma

If you don't know what the prisoner's dilemma is, watch [this video](https://youtu.be/mScpHTIi-kM?si=H1WkStG3r55WDlnP).  
Even if you don’t care about it — **watch it anyway**. I promise you'll be fascinated.

But if you're lazy, here’s a **very rough, concise** explanation:

#### game theory

Suppose Earth is at war with aliens. They play a game called *prisoner’s dilemma*. The rules are:

1. **Both cooperate** → There will be peace.  
2. **One defects** → The other side loses.  
3. **Both defect** → There is war (and let’s be real — Earth has no chance).

**Game theory** is just the math behind these kinds of decisions. Sounds simple — but it gets deep, fast.

---

#### simulation in python

There are many strategies in this game — like:
- `always_cooperate`
- `always_defect`
- `tit_for_tat`
- `random_choice`

In my Python simulation:
- Each strategy plays against every other.
- Each game runs for a **random number of rounds (1–1000)**.
- Points are **unpredictable**, to mimic real-world chaos.

And the wildest part?

> **"Tit for Tat" always wins.**  
> No matter how much you try to trick it.  
> No matter how random things get.  
> In the long run — it's the most successful.

##### the maths behind the concept of *Game Theory* is one of the most fascinating things you can ever encounter. if you want to add some strategies of your own just fork the repo and add a class in `strategy.py`, as well as in list in the end of file. and don't forget to do `pip install -r requirements.txt`
