"""
Biology Flashcards Generator
----------------------------
Single-file Python CLI for generating, viewing, saving, and quizzing on biology flashcards.

Features:
- Built-in example chapters: Plant Physiology, Cell Organelles, Biomolecules
- Ask for a chapter name to generate Q&A flashcards
- Add new flashcards to a chapter
- Save / Load flashcards to JSON (flashcards_db.json)
- Export a chapter's flashcards to a plain text file
- Quiz mode to test yourself

Usage:
$ python biology_flashcards_generator.py

Notes:
- Uses a local JSON file (flashcards_db.json) in the same folder to persist user additions.
- Safe for beginners: no external dependencies (works with Python 3.7+).

"""

import json
import os
import random
import textwrap
from typing import Dict, List, Tuple

DB_FILENAME = "flashcards_db.json"

# --- Starter data ---
DEFAULT_DB: Dict[str, List[Dict[str, str]]] = {
    "Plant Physiology": [
        {
            "question": "What is photosynthesis?",
            "answer": "Photosynthesis is the process by which green plants use sunlight to synthesize foods (glucose) from carbon dioxide and water, releasing oxygen as a byproduct."
        },
        {
            "question": "Name the pigment primarily responsible for photosynthesis.",
            "answer": "Chlorophyll (mainly chlorophyll a and b)."
        },
        {
            "question": "What is transpiration?",
            "answer": "Transpiration is the process of water vapor loss from plant aerial parts, mainly through stomata."
        }
    ],
    "Cell Organelles": [
        {
            "question": "What is the function of mitochondria?",
            "answer": "Mitochondria are the powerhouse of the cell; they produce ATP through cellular respiration."
        },
        {
            "question": "Which organelle is responsible for protein synthesis?",
            "answer": "Ribosomes (free or bound to the rough ER)."
        },
        {
            "question": "What is the role of the Golgi apparatus?",
            "answer": "The Golgi apparatus modifies, sorts, and packages proteins and lipids for storage or transport out of the cell."
        }
    ],
    "Biomolecules": [
        {
            "question": "What are the four major classes of biomolecules?",
            "answer": "Carbohydrates, lipids, proteins, and nucleic acids."
        },
        {
            "question": "What is the monomer of proteins?",
            "answer": "Amino acids."
        },
        {
            "question": "What is the primary function of carbohydrates?",
            "answer": "Provide energy and structural support (e.g., cellulose in plants)."
        }
    ],
    "Genetics": [
        {
            "question": "What is DNA?",
            "answer": "DNA (deoxyribonucleic acid) is the molecule that carries genetic instructions used in growth, development, functioning, and reproduction of all living organisms."
        },
        {
            "question": "What are genes?",
            "answer": "Genes are segments of DNA that contain the instructions for building proteins."
        },
        {
            "question": "What is the difference between genotype and phenotype?",
            "answer": "Genotype refers to the genetic makeup of an organism, while phenotype refers to the observable characteristics or traits."
        }
    ],
    "Human Physiology": [
        {
            "question": "What is homeostasis?",
            "answer": "Homeostasis is the process by which the body maintains a stable internal environment despite changes in external conditions."
        },
        {
            "question": "Name the main components of the human circulatory system.",
            "answer": "The heart, blood vessels (arteries, veins, capillaries), and blood."
        },
        {
            "question": "What is the function of the respiratory system?",
            "answer": "The respiratory system facilitates gas exchange, allowing oxygen to enter the blood and carbon dioxide to be expelled from the body."
        }
    ],
    "Ecology": [
        {
            "question": "What is an ecosystem?",
            "answer": "An ecosystem is a community of living organisms interacting with their physical environment."
        },
        {
            "question": "Define biodiversity.",
            "answer": "Biodiversity refers to the variety of life in a particular habitat or ecosystem."
        },
        {
            "question": "What is the role of producers in an ecosystem?",
            "answer": "Producers, such as plants and algae, convert solar energy into chemical energy through photosynthesis, forming the base of the food chain."
        }
    ],
    "Microbiology": [
        {
            "question": "What are bacteria?",
            "answer": "Bacteria are single-celled microorganisms that can exist either as independent organisms or as parasites."
        },
        {
            "question": "What is a virus?",
            "answer": "A virus is a small infectious agent that replicates only inside the living cells of an organism."
        },
        {
            "question": "Name two beneficial roles of microbes.",
            "answer": "Decomposing organic matter and aiding in digestion (e.g., gut microbiota)."
        }
    ],
    "Evolution": [
        {
            "question": "What is natural selection?",
            "answer": "Natural selection is the process by which organisms better adapted to their environment tend to survive and produce more offspring."
        },
        {
            "question": "Who proposed the theory of evolution by natural selection?",
            "answer": "Charles Darwin."
        },
        {
            "question": "What is genetic drift?",
            "answer": "Genetic drift is a mechanism of evolution that refers to random changes in the frequency of alleles in a population."
        }
    ],
    "Cell Division": [
        {
            "question": "What are the two main types of cell division?",
            "answer": "Mitosis and meiosis."
        },
        {
            "question": "What is the purpose of mitosis?",
            "answer": "Mitosis is for growth, repair, and asexual reproduction, producing two identical daughter cells."
        },
        {
            "question": "How does meiosis differ from mitosis?",
            "answer": "Meiosis produces four genetically diverse haploid cells (gametes) for sexual reproduction, while mitosis produces two identical diploid cells."
        }
    ],
    "Enzymes": [
        {
            "question": "What are enzymes?",
            "answer": "Enzymes are biological catalysts that speed up chemical reactions in living organisms."
        },
        {
            "question": "What is the active site of an enzyme?",
            "answer": "The active site is the region of an enzyme where substrate molecules bind and undergo a chemical reaction."
        },
        {
            "question": "How do temperature and pH affect enzyme activity?",
            "answer": "Extreme temperatures and pH levels can denature enzymes, reducing their activity or rendering them inactive."
        }
    ],
    "Photosynthesis": [
        {
            "question": "What are the two main stages of photosynthesis?",
            "answer": "The light-dependent reactions and the Calvin cycle (light-independent reactions)."
        },
        {
            "question": "Where in the cell does photosynthesis occur?",
            "answer": "In the chloroplasts of plant cells."
        },
        {
            "question": "What are the main products of photosynthesis?",
            "answer": "Glucose (C6H12O6) and oxygen (O2)."
        }
    ],
    "Respiration": [
        {
            "question": "What is cellular respiration?",
            "answer": "Cellular respiration is the process by which cells convert glucose and oxygen into energy (ATP), carbon dioxide, and water."
        },
        {
            "question": "What are the three main stages of cellular respiration?",
            "answer": "Glycolysis, the Krebs cycle (citric acid cycle), and the electron transport chain."
        },
        {
            "question": "Where does glycolysis occur in the cell?",
            "answer": "In the cytoplasm."
        }
    ],
    "Immune System": [
        {
            "question": "What are the two main types of immunity?",
            "answer": "Innate (nonspecific) immunity and adaptive (specific) immunity."
        },
        {
            "question": "What is the role of antibodies?",
            "answer": "Antibodies are proteins produced by B cells that recognize and neutralize pathogens such as bacteria and viruses."
        },
        {
            "question": "What are T cells?",
            "answer": "T cells are a type of lymphocyte that play a central role in cell-mediated immunity."
        }
    ],
    "Nervous System": [
        {
            "question": "What is the main function of the nervous system?",
            "answer": "The nervous system coordinates the body's responses to internal and external stimuli through electrical and chemical signals."
        },
        {
            "question": "What are neurons?",
            "answer": "Neurons are specialized cells that transmit nerve impulses."
        },
        {
            "question": "What is the difference between the central and peripheral nervous systems?",
            "answer": "The central nervous system (CNS) consists of the brain and spinal cord, while the peripheral nervous system (PNS) includes all other neural elements outside the CNS."
        }
    ],
    "Water and pH in Biology": [
        {
            "question": "Why is water essential for life?",
            "answer": "Water is a universal solvent, helps regulate temperature, and is involved in many biochemical reactions."
        },
        {
            "question": "What is pH?",
            "answer": "pH is a measure of the hydrogen ion concentration in a solution, indicating its acidity or alkalinity."
        },
        {
            "question": "What pH range is considered neutral?",
            "answer": "A pH of 7 is considered neutral."
        }
    ],
    "Genetic Engineering": [
        {
            "question": "What is genetic engineering?",
            "answer": "Genetic engineering is the direct manipulation of an organism's genes using biotechnology."
        },
        {
            "question": "What is a common tool used in genetic engineering?",
            "answer": "CRISPR-Cas9 is a widely used tool for gene editing."
        },
        {
            "question": "What are GMOs?",
            "answer": "GMOs (genetically modified organisms) are organisms whose genetic material has been altered using genetic engineering techniques."
        }
    ],
    "Cell Membrane": [
        {
            "question": "What is the structure of the cell membrane?",
            "answer": "The cell membrane is composed of a phospholipid bilayer with embedded proteins, cholesterol, and carbohydrates."
        },
        {
            "question": "What is the function of the cell membrane?",
            "answer": "The cell membrane regulates the movement of substances in and out of the cell and provides protection and support."
        },
        {
            "question": "What is selective permeability?",
            "answer": "Selective permeability refers to the ability of the cell membrane to allow certain molecules to pass through while blocking others."
        }
    ],
    "Photosynthetic Pigments": [
        {
            "question": "What are the main types of photosynthetic pigments?",
            "answer": "Chlorophylls, carotenoids, and phycobilins."
        },
        {
            "question": "What is the role of carotenoids in photosynthesis?",
            "answer": "Carotenoids protect chlorophyll from photo-damage and assist in light absorption."
        },
        {
            "question": "Where are photosynthetic pigments located in plant cells?",
            "answer": "In the thylakoid membranes of chloroplasts."
        }
    ],
    "Hormones in Plants": [
        {
            "question": "What are plant hormones?",
            "answer": "Plant hormones are chemical messengers that regulate various physiological processes in plants."
        },
        {
            "question": "Name four major plant hormones.",
            "answer": "Auxins, gibberellins, cytokinins, and abscisic acid."
        },
        {
            "question": "What is the role of auxins in plants?",
            "answer": "Auxins promote cell elongation, root initiation, and are involved in phototropism and gravitropism."
        }
    ],
    "DNA Replication": [
        {
            "question": "What is DNA replication?",
            "answer": "DNA replication is the process by which a cell duplicates its DNA before cell division."
        },
        {
            "question": "Name the enzyme responsible for synthesizing new DNA strands.",
            "answer": "DNA polymerase."
        },
        {
            "question": "What is the significance of the semi-conservative model of DNA replication?",
            "answer": "In the semi-conservative model, each new DNA molecule consists of one original strand and one newly synthesized strand, ensuring genetic continuity."
        }
    ],
    "Protein Synthesis": [
        {
            "question": "What are the two main processes of protein synthesis?",
            "answer": "Transcription and translation."
        },
        {
            "question": "Where does transcription occur in eukaryotic cells?",
            "answer": "In the nucleus."
        },
        {
            "question": "What is the role of mRNA in protein synthesis?",
            "answer": "mRNA (messenger RNA) carries the genetic code from DNA to the ribosomes for protein assembly."
        }
    ],
    "Cell Cycle": [
        {
            "question": "What are the main phases of the cell cycle?",
            "answer": "Interphase (G1, S, G2) and M phase (mitosis and cytokinesis)."
        },
        {
            "question": "What happens during the S phase of interphase?",
            "answer": "DNA replication occurs, resulting in two identical sets of chromosomes."
        },
        {
            "question": "What is the purpose of checkpoints in the cell cycle?",
            "answer": "Checkpoints ensure that the cell is ready to proceed to the next phase, preventing errors such as DNA damage from being passed on."
        }
    ],
    "Enzyme Inhibition": [
        {
            "question": "What is enzyme inhibition?",
            "answer": "Enzyme inhibition is the process by which a molecule decreases or stops the activity of an enzyme."
        },
        {
            "question": "What are the two main types of enzyme inhibition?",
            "answer": "Competitive and non-competitive inhibition."
        },
        {
            "question": "How does competitive inhibition work?",
            "answer": "In competitive inhibition, an inhibitor molecule binds to the active site of the enzyme, preventing substrate binding."
        }
    ],
    "Membrane Transport": [
        {
            "question": "What are the two main types of membrane transport?",
            "answer": "Passive transport and active transport."
        },
        {
            "question": "What is osmosis?",
            "answer": "Osmosis is the diffusion of water molecules across a semipermeable membrane from an area of lower solute concentration to an area of higher solute concentration."
        },
        {
            "question": "What is the difference between facilitated diffusion and active transport?",
            "answer": "Facilitated diffusion is a passive process that uses transport proteins to move substances down their concentration gradient, while active transport requires energy (ATP) to move substances against their concentration gradient."
        }
    
    ]
}

# --- File handling ---

def load_db(filename: str = DB_FILENAME) -> Dict[str, List[Dict[str, str]]]:
    """Load the flashcard database from JSON, or return defaults if file missing/corrupt."""
    if not os.path.exists(filename):
        return DEFAULT_DB.copy()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Ensure proper structure
        if isinstance(data, dict):
            return data
        else:
            print("Warning: DB file malformed — using defaults.")
            return DEFAULT_DB.copy()
    except Exception as e:
        print(f"Error loading DB: {e}\nUsing default data.")
        return DEFAULT_DB.copy()


def save_db(db: Dict[str, List[Dict[str, str]]], filename: str = DB_FILENAME) -> None:
    """Save the flashcard database to JSON."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving DB: {e}")

# --- Flashcard operations ---

def list_chapters(db: Dict[str, List[Dict[str, str]]]) -> List[str]:
    return sorted(db.keys())


def get_flashcards(db: Dict[str, List[Dict[str, str]]], chapter: str) -> List[Dict[str, str]]:
    return db.get(chapter, [])


def add_flashcard(db: Dict[str, List[Dict[str, str]]], chapter: str, question: str, answer: str) -> None:
    if chapter not in db:
        db[chapter] = []
    db[chapter].append({"question": question.strip(), "answer": answer.strip()})


def export_to_text(flashcards: List[Dict[str, str]], chapter: str, filename: str = None) -> str:
    if filename is None:
        safe_name = chapter.replace(" ", "_")
        filename = f"{safe_name}_flashcards.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Flashcards — {chapter}\n")
        f.write("=" * (len(chapter) + 13) + "\n\n")
        for i, fc in enumerate(flashcards, 1):
            f.write(f"Q{i}: {fc['question']}\n")
            f.write(f"A{i}: {fc['answer']}\n\n")
    return filename

# --- Generator ---

def generate_flashcards_for_chapter(db: Dict[str, List[Dict[str, str]]], chapter: str, n: int = None) -> List[Dict[str, str]]:
    pool = get_flashcards(db, chapter)
    if not pool:
        return []
    if n is None or n >= len(pool):
        return pool.copy()
    return random.sample(pool, n)

# --- Quiz mode ---

def quiz_user(flashcards: List[Dict[str, str]], rounds: int = 5) -> None:
    if not flashcards:
        print("No flashcards to quiz on.")
        return
    rounds = min(rounds, len(flashcards))
    pool = flashcards.copy()
    random.shuffle(pool)
    score = 0
    for i in range(rounds):
        q = pool[i]
        print(f"\nQuestion {i+1}:\n{q['question']}")
        input("Press Enter to reveal the answer...")
        print(textwrap.fill(f"Answer: {q['answer']}", width=80))
        correct = input("Did you get it right? (y/n) ").strip().lower()
        if correct.startswith("y"):
            score += 1
    print(f"\nQuiz finished — Score: {score}/{rounds}")

# --- Utility for clean input ---

def prompt_nonempty(prompt_text: str) -> str:
    while True:
        s = input(prompt_text).strip()
        if s:
            return s
        print("Please enter a non-empty value.")

# --- CLI/menu ---

def main_menu():
    db = load_db()
    print("\n=== Biology Flashcards Generator ===\n")

    while True:
        print("Options:\n 1) List chapters\n 2) View chapter flashcards\n 3) Generate (sample) flashcards\n 4) Add flashcard\n 5) Export chapter to text file\n 6) Quiz mode\n 7) Save DB\n 8) Exit")
        choice = input("Choose an option [1-8]: ").strip()

        if choice == "1":
            chapters = list_chapters(db)
            print("\nAvailable chapters:")
            for c in chapters:
                print(f" - {c} ({len(db.get(c, []))} cards)")
            print()

        elif choice == "2":
            chapter = prompt_nonempty("Enter chapter name: ")
            cards = get_flashcards(db, chapter)
            if not cards:
                print(f"No flashcards found for '{chapter}'.\n")
            else:
                print(f"\nFlashcards for '{chapter}':\n")
                for i, fc in enumerate(cards, 1):
                    print(f"Q{i}: {fc['question']}")
                    print(f"A{i}: {fc['answer']}\n")

        elif choice == "3":
            chapter = prompt_nonempty("Enter chapter name: ")
            n_str = input("How many cards to generate (Enter for all): ").strip()
            n = int(n_str) if n_str.isdigit() else None
            sample = generate_flashcards_for_chapter(db, chapter, n)
            if not sample:
                print(f"No flashcards found for '{chapter}'.\n")
            else:
                print(f"\nGenerated {len(sample)} flashcards from '{chapter}':\n")
                for i, fc in enumerate(sample, 1):
                    print(f"Q{i}: {fc['question']}")
                    print(f"A{i}: {fc['answer']}\n")

        elif choice == "4":
            chapter = prompt_nonempty("Enter chapter name to add to: ")
            question = prompt_nonempty("Enter question: ")
            answer = prompt_nonempty("Enter answer: ")
            add_flashcard(db, chapter, question, answer)
            print("Flashcard added. (Don't forget to save with option 7.)\n")

        elif choice == "5":
            chapter = prompt_nonempty("Enter chapter name to export: ")
            cards = get_flashcards(db, chapter)
            if not cards:
                print(f"No flashcards found for '{chapter}'.\n")
            else:
                filename = export_to_text(cards, chapter)
                print(f"Exported to {filename}\n")

        elif choice == "6":
            chapter = prompt_nonempty("Enter chapter name for quiz: ")
            cards = get_flashcards(db, chapter)
            if not cards:
                print(f"No flashcards found for '{chapter}'.\n")
            else:
                rounds_str = input("How many questions? [default 5]: ").strip()
                rounds = int(rounds_str) if rounds_str.isdigit() else 5
                quiz_user(cards, rounds)

        elif choice == "7":
            save_db(db)
            print(f"Database saved to {DB_FILENAME}\n")

        elif choice == "8":
            save_prompt = input("Save changes before exit? (y/n) [y]: ").strip().lower()
            if save_prompt in ("", "y", "yes"):
                save_db(db)
                print(f"Database saved to {DB_FILENAME}")
            print("Goodbye!")
            break

        else:
            print("Invalid option — please choose a number between 1 and 8.\n")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted — exiting. (Any unsaved changes may be lost.)")
