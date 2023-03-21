import os

transcript_files = os.listdir("..\Raw Transcripts")

for transcript in transcript_files:
    print("Cleaning up", transcript)
    transcript_filename = transcript
    orig_file = open("..\Raw Transcripts\\" + transcript_filename, encoding="utf-8")
    orig_file_lines = orig_file.readlines()

    newfile = open("..\Experiment Transcripts\\" + transcript_filename, 'w', encoding="utf-8")

    for line in orig_file_lines:
        if not line == "\n":
            newfile.write(line.lstrip())

    orig_file.close()
    newfile.close()