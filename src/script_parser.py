import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

setup_prompt = "Find the interactions between characters from a given portion of a movie transcript. For each interaction that you find, output it as Character1, Character2. Below is the transcript to analyze:\n"

script_portion = """[1989 – Hank Pym enters a SHIELD facility and storms S.H.I.E.L.D's board room in the Triskelion]
Dr. Hank Pym: Stark.
Mitchell Carson: He doesn’t seem happy.
Howard Stark: Hello, Hank. You’re supposed to be in Moscow.
Dr. Hank Pym: I took a detour. [he places a vial containing a red serum on the table] Through your defense lab.
Peggy Carter: Tell me that isn’t what I think it is.
Dr. Hank Pym: It depends, if you think it’s a poor attempt to replicate my work. Even for this group, that takes nerve.
Mitchell Carson: You were instructed to go to Russia. May I remind you, Dr. Pym, that you’re a soldier…
Dr. Hank Pym: I’m a scientist.
Howard Stark: Then act like one. The Pym Particle is the most revolutionary science ever developed, help us put it to good use.
Dr. Hank Pym: I let you turn me into your errand boy, and now you try to steal my research?
Mitchell Carson: If only you’d protected Janet with such ferocity, Dr. Pym.
Dr. Hank Pym: Oh, god. [suddenly Pym slams down Carson’s face on the table in anger, Peggy pulls him away]
Peggy Carter: Easy, Hank.
Dr. Hank Pym: You mention my wife again and I’ll show you ferocity. [Carson looks at Stark as he wipes blood from his nose]
Howard Stark: Don’t look at me, you said it.
Dr. Hank Pym: I formally tender my resignation.
Howard Stark: We don’t accept it. Formally. Hank, we need you. The Pym Particle is a miracle. Please, don’t let your past determine the future.
Dr. Hank Pym: As long as I am alive, nobody will ever get that formula. [Pym turns around and leaves calmly]
Mitchell Carson: We shouldn’t let him leave the building.
Peggy Carter: You’ve already lied to him, now you want to go to war with him?
Mitchell Carson: Yes! Our scientists haven’t come close to replicating his work.
Howard Stark: He just kicked your ass full size. You really want to find out what it’s like when you can’t see him coming? I’ve known Hank Pym for a long time, he’s no security risk. Unless we make him one.
"""

# prompt = "What color should I wear on St. Patricks Day?"

# print((setup_prompt + script_portion))

# response = openai.Completion.create(
#     model="gpt-3.5-turbo",
#     prompt=(setup_prompt + script_portion),
#     max_tokens=1000,
#     temperature=0.5
# )

# print(response)

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": (setup_prompt + script_portion)}],
    temperature=0.5,
    max_tokens=1000
)

print(response)

print(response.choices[0].message.content)
