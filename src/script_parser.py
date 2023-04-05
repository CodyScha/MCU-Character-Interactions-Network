import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# * Setup some variables that we will use throughout the program.
setup_prompt = "Find the interactions between characters from a given portion of a movie transcript. For each interaction that you find, output it as Character1, Character2 with no other details or output. Below is the transcript to analyze:\n"
chunk_size = 100

# * Get all of the files in the Experiment Transcripts dir
transcripts = os.listdir('..\Experiment Transcripts')

# * To keep track of the CSVs that we have already parsed
finished_CSVs = [name.split(".")[0] for name in os.listdir("../Movie CSVs")]

for movie_file_name in transcripts:
    movie_title = movie_file_name.split(".")[0]
    if not movie_title in finished_CSVs:
        print("Begin parsing of", movie_file_name)

        # * Open the movie
        movie_file = open('..\Experiment Transcripts\\' + movie_file_name, encoding="utf-8")
        movie_lines = movie_file.readlines()

        movie_chunks = [movie_lines[x:x+chunk_size] for x in range(0, len(movie_lines), chunk_size)]

        # * Split the movie file name and create a new name for the CSV
        csv_name = movie_file_name.split(".")[0] + ".csv"

        # * Make a new CSV file
        output_csv = open("../Movie CSVs/" + csv_name, 'w', encoding="utf-8")

        chunk_num = 0
        for chunk in movie_chunks:
            print("On Chunk #", chunk_num)

            # * Combine the chunk bits into a single string
            script_portion = ""
            for line in chunk:
                script_portion += line

            # * With the complete script portion, lets call the API
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role": "user", "content": (setup_prompt + script_portion)}],
                temperature=0.5,
                max_tokens=175
            )

            # * Now that we have our response, we should write that to a file
            output_csv.write(response.choices[0].message.content)

            print("Chunk #", chunk_num, " prompt tokens: ", response.usage.prompt_tokens)
            print("Chunk #", chunk_num, " answer tokens: ", response.usage.completion_tokens)
            print("Chunk #", chunk_num, " total tokens: ", response.usage.total_tokens)
            
            chunk_num +=1