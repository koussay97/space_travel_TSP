<!-- @format -->

# 🚀 Simulating Space Travel with TSP & Physics! 🌍✨

In the world of fancy space travel, I’ve been working on a project that simulates interplanetary journeys using a set of spaceships and applies the Traveling Salesman Problem (TSP) to identify the best Hamiltonian tour across all planets—returning to the starting node: Planet Earth 🌎.

---
## 🚀 The Journey: Three Key Phases

### 1️⃣ Crossing the Atmosphere ☁️🔝

**Force equation:**
```math
F_{net} = F_{thrust} - F_{gravity} - F_{air friction}
```
_Valid while the spaceship is within atmospheric altitude._

---
### 2️⃣ Landing on a Planet 🏁🌕

**Force equation:**
```math
F_{net} = F_{thrust} - F_{gravity} + F_{air friction}
```

**Time calculation using acceleration and kinematic equations:**
```math
t = \sqrt{\frac{2 \times \text{atmosphere altitude}}{|\text{acceleration}|}}
```

#### ✨ Assumptions:
- Air friction and gravity remain constant for simplicity.
- Ships with `F(net) < 0` are deemed mechanically unfit, triggering an exception with a stack trace detailing the ship, planet, and failure reason.

---
### 3️⃣ Interplanetary Travel 🌌🛰

#### Simplifications:
- ✅ Planets remain stationary (no orbiting).
- ✅ No gravitational influence from planets on the spaceship.
- ✅ Engine thrust power is constant with an infinite energy source.

_This may be unrealistic, but the goal is to identify the most powerful engines capable of operating across all planets._

---
## 🔥 Adding Some Fun!
We threw the **Millennium Falcon** 🛸 (from Star Wars) into the mix—no hyperdrive, just its estimated **10,000 kg mass** and **3M Newton thrust power**!

### 🏆 The Best Performer: **SpaceX Merlin 1D (Falcon 9)** 🚀
Due to its exceptional mass-to-thrust ratio, the **Falcon 9 engine** outperforms all other ships in acceleration, atmosphere traversal, and planetary landings.

⏳ _With constant thrust and no external forces, it could complete a full Hamiltonian cycle across the entire solar system in **786.78 years**—assuming an infinite energy source._

---
## 🎮 Final Verdict: **GG, Elon Musk!** 🚀
Would love to hear your thoughts! What other factors should be included in the next iteration of this simulation? 🤔💡

---
## 🛠 Installation Scripts

### 🔹 Create Virtual Environment
```sh
python -m venv .myVnV
```

### 🔹 Activate Virtual Environment
```sh
# PowerShell
.\.myVnV\Scripts\Activate.ps1

# CMD
env\Scripts\activate

# To deactivate
deactivate
```

_**Debugging Tip:**_
```sh
Get-ChildItem -Recurse -Filter "activate" -Directory ollamaEnv
```

### 🔹 Install Dependencies
```sh
pip cache purge
pip install -r requirements.txt
```

#### In case of failure:
```sh
pip cache purge
pip install -r requirements.txt -i https://pypi.org/simple --timeout 120
```

#### Force reinstall if necessary:
```sh
pip install --force-reinstall -r requirements.txt
```

### 🔹 Verify Installed Dependencies
```sh
pip list
```

