import random
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Global lists to store adjectives and nouns
adjectives = [
    "broken", "endless", "lost", "faded", "dreamy", "longing", "silent", "beautiful", "unspoken", 
    "forgotten", "lonely", "wild", "hopeful", "tragic", "new", "ancient", "melancholic", "nostalgic",
    "passionate", "heartfelt", "sweet", "mysterious", "turbulent", "shattered", "vivid", "untold",
    "haunting", "restless", "distant", "fragile", "heavy", "golden", "stormy", "brilliant", "forlorn",
    "bitter", "strange", "hidden", "timeless", "soothing", "gentle", "fleeting", "warm",
    "tender", "dark", "vibrant", "invisible", "forgotten", "eternal", "vulnerable", "wistful", "defiant",
    "daring", "unexpected", "shy", "fiery", "quiet", "intimate", "sincere", "blazing", "unpredictable",
    "glorious", "spontaneous", "unforgettable", "fragile", "hopeful"
]

nouns = [
    "tragedy", "heartbreak", "confession", "reflection", "desire", "regret", "loss", "hope", "dream", "journey", 
    "fear", "loneliness", "love", "memory", "passion", "betrayal", "freedom", "pain", "truth", "vulnerability", 
    "change", "grief", "faith", "forgiveness", "moment", "connection", "opportunity", "longing", "escape", 
    "struggle", "awakening", "revelation", "realization", "challenge", "sacrifice", "solitude", "rebirth", "fate", 
    "choice", "growth", "strength", "temptation", "battle", "conflict", "yearning", "desperation", "uncertainty", 
    "fall", "rise", "path", "clash", "decision", "turning point", "momentum", "voice", "doubt", "dreamer", 
    "faith", "opportunity", "struggle", "awakening", "transformation", "realization", "addiction", "nightmares", 
    "chaos", "void", "despair", "anxiety", "anguish", "misery", "solitude", "drowning", "paranoia", 
    "nightfall", "cynicism", "escape", "emptiness", "regret", "unrest", "overcome", "lost", "betrayed", 
    "heart", "healing", "madness", "illusion", "soul", "shame", "detachment", "mourning", "self-reflection", 
    "wasted", "disconnection", "scar", "dreams", "fragile", "toxin", "misunderstood", "chaos", "devastation", 
    "disillusion", "confusion", "doubt", "pain", "emptiness", "grief", "trapped", "blowback", 

    # Mafioso-themed nouns
    "empire", "crown", "throne", "deal", "trust", "betrayal", "honor", "family", 
    "loyalty", "revenge", "street", "blood", "gang", "soldier", "hustle", "power", "reign", "crime", 
    "danger", "legacy", "money", "fortune", "clout", "respect", "enemies", "kill", "trap", "whistleblower", 
    "backstabber", "underworld", "hit", "bounty", "bribe", "snitch", "darkness", "treachery", 
    "loyalist", "murder", "dealership", "smuggler", "criminal", "game", "grind", "dirt", "fire", 
    "war", "shakedown", "payback", "witness", "contract", "bust", "violence", "allegiance", 
    "trigger", "scheme", "debt", "bloodshed", "law", "gangster", "fame", "payday", "heist", "sting", 
    "oath", "survival", "blowback",

    # Anime & Ninja-themed nouns
    "honor", "master", "clan", "warrior", "blade", "fist", 
    "shadow", "spirit", "destiny", "power", "demon", "soul", "ghost", "flame", "phoenix", 
    "dragon", "legend", "journey", "vow", "stealth", "technique", "village", 
    "ronin", "battle", "warlord", "realm", "sacrifice", "serpent",
    "wave", "thunder", "storm", "wind", "abyss", "clash", "bloodline", "legacy", "talisman", "throne", 
    "temple", "prophecy", "reaper", "struggle", "raven", "emperor", "honor", "fate", "curse", "rebirth", 
    "soulmate", "exile", "vision", "rebellion"
]

def get_random_word(part_of_speech):
    """Fetch a random word of the specified part of speech from the lists."""
    if part_of_speech == "adj":
        return random.choice(adjectives)
    elif part_of_speech == "n":
        return random.choice(nouns)
    else:
        return None

def generate_prompt():
    """Generate a random songwriting prompt using an adjective and noun."""
    adjective = get_random_word("adj")
    noun = get_random_word("n")

    if adjective and noun:
        return f"Song topic: {adjective} {noun}"
    else:
        return "Failed to generate a prompt. Try again!"

# Create the main window for the GUI
def show_gui():
    def on_generate():
        prompt = generate_prompt()
        prompt_label.config(text=prompt)

    def open_settings():
        settings_window = tk.Toplevel(root)
        settings_window.title("Edit Word Lists")

        def save_changes():
            nonlocal adjective_entry, noun_entry
            # Update the global lists
            adjectives.clear()
            adjectives.extend(adjective_entry.get().split(","))
            nouns.clear()
            nouns.extend(noun_entry.get().split(","))
            messagebox.showinfo("Saved", "Your changes have been saved.")

        # Create the form to edit the lists
        adjective_label = tk.Label(settings_window, text="Edit Adjectives (comma separated):")
        adjective_label.pack(pady=5)
        adjective_entry = tk.Entry(settings_window, width=50)
        adjective_entry.insert(0, ", ".join(adjectives))
        adjective_entry.pack(pady=5)

        noun_label = tk.Label(settings_window, text="Edit Nouns (comma separated):")
        noun_label.pack(pady=5)
        noun_entry = tk.Entry(settings_window, width=50)
        noun_entry.insert(0, ", ".join(nouns))
        noun_entry.pack(pady=5)

        save_button = tk.Button(settings_window, text="Save Changes", command=save_changes)
        save_button.pack(pady=20)

    root = tk.Tk()
    root.title("Songwriting Prompt Generator")

    # Add a menu for settings
    menu_bar = tk.Menu(root)
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Edit Word Lists", command=open_settings)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)
    root.config(menu=menu_bar)

    # Create the main label and generate button
    prompt_label = tk.Label(root, text="Click the button to generate a songwriting prompt!", width=40, height=4, wraplength=400)
    prompt_label.pack(pady=20)

    generate_button = tk.Button(root, text="Generate Prompt", command=on_generate, height=2, width=20)
    generate_button.pack(pady=10)

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    show_gui()
