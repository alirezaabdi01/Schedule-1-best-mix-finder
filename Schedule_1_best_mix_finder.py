############################################
#                                          #
# Made By https://github.com/alirezaabdi01 #
#                                          #
############################################

import math, time, os, json, argparse
from itertools import product, islice
from multiprocessing import Pool, cpu_count, current_process

# ─────────────────────────── data blocks (unchanged) ───────────────────────────
ingredients = {
    'Addy': {
        'base_effect': 'Thought-Provoking',
        'price': 9,
        'reactions': {
            'Explosive': 'Euphoric',
            'Foggy': 'Energizing',
            'Glowing': 'Refreshing',
            'Long Faced': 'Electrifying',
            'Sedating': 'Gingeritis'
        }
    },
    'Banana': {
        'base_effect': 'Gingeritis',
        'price': 2,
        'reactions': {
            'Calming': 'Sneaky',
            'Cyclopean': 'Energizing',
            'Disorienting': 'Focused',
            'Energizing': 'Thought-Provoking',
            'Focused': 'Seizure-Inducing',
            'Long Faced': 'Refreshing',
            'Paranoia': 'Jennerising',
            'Smelly': 'Anti-Gravity',
            'Toxic': 'Smelly'
        }
    },
    'Battery': {
        'base_effect': 'Bright-Eyed',
        'price': 8,
        'reactions': {
            'Cyclopean': 'Glowing',
            'Electrifying': 'Euphoric',
            'Euphoric': 'Zombifying',
            'Laxative': 'Calorie-Dense',
            'Munchies': 'Tropic Thunder',
            'Shrinking': 'Munchies'
        }
    },
    'Chili': {
        'base_effect': 'Spicy',
        'price': 7,
        'reactions': {
            'Anti-Gravity': 'Tropic Thunder',
            'Athletic': 'Euphoric',
            'Laxative': 'Long Faced',
            'Munchies': 'Toxic',
            'Shrinking': 'Refreshing',
            'Sneaky': 'Bright-Eyed'
        }
    },
    'Cuke': {
        'base_effect': 'Energizing',
        'price': 2,
        'reactions': {
            'Euphoric': 'Laxative',
            'Foggy': 'Cyclopean',
            'Gingeritis': 'Thought-Provoking',
            'Munchies': 'Athletic',
            'Slippery': 'Munchies',
            'Sneaky': 'Paranoia',
            'Toxic': 'Euphoric'
        }
    },
    'Donut': {
        'base_effect': 'Calorie-Dense',
        'price': 3,
        'reactions': {
            'Anti-Gravity': 'Slippery',
            'Balding': 'Sneaky',
            'Calorie-Dense': 'Explosive',
            'Focused': 'Euphoric',
            'Jennerising': 'Gingeritis',
            'Munchies': 'Calming',
            'Shrinking': 'Energizing'
        }
    },
    'Energy Drink': {
        'base_effect': 'Athletic',
        'price': 6,
        'reactions': {
            'Disorienting': 'Electrifying',
            'Euphoric': 'Energizing',
            'Focused': 'Shrinking',
            'Foggy': 'Laxative',
            'Glowing': 'Disorienting',
            'Schizophrenia': 'Balding',
            'Sedating': 'Munchies',
            'Spicy': 'Euphoric',
            'Tropic Thunder': 'Sneaky'
        }
    },
    'Flu Medicine': {
        'base_effect': 'Sedating',
        'price': 5,
        'reactions': {
            'Athletic': 'Munchies',
            'Calming': 'Bright-Eyed',
            'Cyclopean': 'Foggy',
            'Electrifying': 'Refreshing',
            'Euphoric': 'Toxic',
            'Focused': 'Calming',
            'Laxative': 'Euphoric',
            'Munchies': 'Slippery',
            'Shrinking': 'Paranoia',
            'Thought-Provoking': 'Gingeritis'
        }
    },
    'Gasoline': {
        'base_effect': 'Toxic',
        'price': 5,
        'reactions': {
            'Disorienting': 'Glowing',
            'Electrifying': 'Disorienting',
            'Energizing': 'Euphoric',
            'Euphoric': 'Spicy',
            'Gingeritis': 'Smelly',
            'Jennerising': 'Sneaky',
            'Laxative': 'Foggy',
            'Munchies': 'Sedating',
            'Paranoia': 'Calming',
            'Shrinking': 'Focused',
            'Sneaky': 'Tropic Thunder'
        }
    },
    'Horse Semen': {
        'base_effect': 'Long Faced',
        'price': 9,
        'reactions': {
            'Anti-Gravity': 'Calming',
            'Gingeritis': 'Refreshing',
            'Seizure-Inducing': 'Energizing',
            'Thought-Provoking': 'Electrifying'
        }
    },
    'Iodine': {
        'base_effect': 'Jennerising',
        'price': 8,
        'reactions': {
            'Calming': 'Balding',
            'Calorie-Dense': 'Gingeritis',
            'Euphoric': 'Seizure-Inducing',
            'Foggy': 'Paranoia',
            'Refreshing': 'Thought-Provoking',
            'Toxic': 'Sneaky'
        }
    },
    'Mega Bean': {
        'base_effect': 'Foggy',
        'price': 7,
        'reactions': {
            'Athletic': 'Laxative',
            'Calming': 'Glowing',
            'Energizing': 'Cyclopean',
            'Focused': 'Disorienting',
            'Jennerising': 'Paranoia',
            'Seizure-Inducing': 'Focused',
            'Shrinking': 'Electrifying',
            'Slippery': 'Toxic',
            'Sneaky': 'Calming',
            'Thought-Provoking': 'Energizing'
        }
    },
    'Motor Oil': {
        'base_effect': 'Slippery',
        'price': 6,
        'reactions': {
            'Energizing': 'Munchies',
            'Euphoric': 'Sedating',
            'Foggy': 'Toxic',
            'Munchies': 'Schizophrenia',
            'Paranoia': 'Anti-Gravity'
        }
    },
    'Mouth Wash': {
        'base_effect': 'Balding',
        'price': 4,
        'reactions': {
            'Calming': 'Anti-Gravity',
            'Calorie-Dense': 'Sneaky',
            'Explosive': 'Sedating',
            'Focused': 'Jennerising'
        }
    },
    'Paracetamol': {
        'base_effect': 'Sneaky',
        'price': 3,
        'reactions': {
            'Calming': 'Slippery',
            'Electrifying': 'Athletic',
            'Energizing': 'Paranoia',
            'Focused': 'Gingeritis',
            'Foggy': 'Calming',
            'Glowing': 'Toxic',
            'Munchies': 'Anti-Gravity',
            'Paranoia': 'Balding',
            'Spicy': 'Bright-Eyed',
            'Toxic': 'Tropic Thunder'
        }
    },
    'Viagor': {
        'base_effect': 'Tropic Thunder',
        'price': 4,
        'reactions': {
            'Athletic': 'Sneaky',
            'Disorienting': 'Toxic',
            'Euphoric': 'Bright-Eyed',
            'Laxative': 'Calming',
            'Shrinking': 'Gingeritis'
        }
    }
}

products = {
    "OG K": {
        "sell_price": 38,
        "effects": ["Calming"]
    },
    "Sour D": {
        "sell_price": 40,
        "effects": ["Refreshing"]
    },
    "Green C": {
        "sell_price": 69,
        "effects": ["Energizing"]
    },
    "Grandaddy P": {
        "sell_price": 44,
        "effects": ["Sedating"]
    },
    "Meth": {
        "sell_price": 70,
        "effects": []
    },
    "Cocaine": {
        "sell_price": 150,
        "effects": []
    }
}

effect_multipliers = {
    "Anti-Gravity": 0.54,
    "Athletic": 0.32,
    "Balding": 0.30,
    "Bright-Eyed": 0.40,
    "Calming": 0.10,
    "Calorie-Dense": 0.28,
    "Cyclopean": 0.56,
    "Disorienting": 0.00,
    "Electrifying": 0.50,
    "Energizing": 0.22,
    "Euphoric": 0.18,
    "Explosive": 0.00,
    "Focused": 0.16,
    "Foggy": 0.36,
    "Gingeritis": 0.20,
    "Glowing": 0.48,
    "Jennerising": 0.42,
    "Laxative": 0.00,
    "Long Faced": 0.52,
    "Munchies": 0.12,
    "Paranoia": 0.00,
    "Refreshing": 0.14,
    "Schizophrenia": 0.00,
    "Sedating": 0.26,
    "Seizure-Inducing": 0.00,
    "Shrinking": 0.60,
    "Slippery": 0.34,
    "Smelly": 0.00,
    "Sneaky": 0.24,
    "Spicy": 0.38,
    "Thought-Provoking": 0.44,
    "Toxic": 0.00,
    "Tropic Thunder": 0.46,
    "Zombifying": 0.58
}


# ─────────────────────────── helpers ───────────────────────────
def batched(iterable, size):
    it = iter(iterable)
    while (chunk := list(islice(it, size))):
        yield chunk


# --- worker‑side constant initialisation -----------------------
def _worker_init(imults):
    global EFFECT_MULTS
    EFFECT_MULTS = imults  # each process keeps its own shared copy


# ─────────────────── effect + profit functions ────────────────────
def apply_effects(chain: tuple[str, ...],
                  base_effects: list[str]) -> list[str]:
    effects, seen = list(base_effects), set(base_effects)
    for ing in chain:
        data = ingredients[ing]
        repl = data['reactions']
        new = [
            repl.get(e, e)
            if repl.get(e) not in seen or repl.get(repl[e]) else e
            for e in effects
        ]
        effects, seen = new, set(new)
        if data['base_effect'] not in seen and len(seen) < 8:
            effects.append(data['base_effect'])
            seen.add(data['base_effect'])
    return effects


def calc_profit(combo, base_eff, sell_price):
    cost  = sum(ingredients[i]['price'] for i in combo)
    effects = apply_effects(combo, base_eff)
    mult  = sum(EFFECT_MULTS.get(e, 0) for e in effects)
    
   ####################################
   #                                  #
   # ****Choose Your Calculation:**** #
   #                                  #
   ####################################
    
   ###########################################################
   #                                                         #
   # MULTIPLIE THE PRICE BY 1.6 AND MAX THE THE PRICE TO 999 #
   #                                                         #
   ###########################################################
    
    # price = min(999, int(sell_price * (1 + mult) * 1.6))
    
   ############################
   #                          #
   # MAX THE THE PRICE TO 999 #
   #                          #
   ############################
    
    # price = min(999, int(sell_price * (1 + mult)))
    
   ############################
   #                          #
   # NORMAL PRICE CALCULATION #
   #                          #
   ############################
    
    price = int(sell_price * (1 + mult))
    
    return price - cost, combo, price, cost

# ─────────────────────────── main search ───────────────────────────
def find_best(prod_key: str,
              k: int,
              batch=500_000,
              save_every=5,
              resume=True):

    sell = products[prod_key]['sell_price']
    base_eff = products[prod_key]['effects']
    names = list(ingredients)
    combos = product(names, repeat=k)
    max_batches = (len(names)**k + batch - 1) // batch
    resume_file = f"{prod_key}_{k}combo_state.json"
    start_batch = 0
    best = (-math.inf, None, None, None)  # profit, combo, price, cost

    if resume and os.path.exists(resume_file):
        with open(resume_file) as f:
            data = json.load(f)
        start_batch = data["done"]
        best = tuple(data["best"])
        combos = islice(combos, start_batch * batch, None)  # skip processed

    last_save = time.time()
    
   #########################################################################
   #                                                                       # 
   # YOU CAN LIMIT CPU CORES FOR CACLULATION HERE:                         #
   # THE PROGRAM IS DESIGNED TO DON'T USE 100% OF CPU TO DON'T HURT THE PC #
   #                                                                       #
   #########################################################################

    with Pool(cpu_count(),
              initializer=_worker_init,
              initargs=(effect_multipliers, )) as pool:
        for bi, chunk in enumerate(batched(combos, batch), start_batch + 1):
            t0 = time.perf_counter()
            result = pool.starmap(calc_profit,
                                  [(c, base_eff, sell) for c in chunk],
                                  chunksize=1000)

            for item in result:
                if best is None or item[0] > best[0]:
                    best = item

            print(f"{bi}/{max_batches} "
                  f"({bi/max_batches*100:0.3f}%) "
                  f"{time.perf_counter()-t0:5.2f}s  "
                  f"best≈{best[0]}")

            # periodic auto‑save
            if time.time() - last_save > save_every:
                with open(resume_file, "w") as f:
                    json.dump({"done": bi, "best": best}, f)
                last_save = time.time()

    profit, combo, price, cost = best
    print(f"\n{k}‑ {prod_key}: {combo}")
    print(f"Price {price}$ | Cost {cost}$ | Profit {profit}$")


# ─────────────────────────── CLI interface ───────────────────────────
if __name__ == "__main__":
    # The first is name: OG K / Sour D / Green C / Grandaddy P / Meth / Cocaine
    # The Second is the amount of ingredients 
    find_best("Meth", 8)