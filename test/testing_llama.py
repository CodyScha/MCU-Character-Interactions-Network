from llama_index import SimpleDirectoryReader, LLMPredictor, GPTSimpleVectorIndex,PromptHelper,ServiceContext
from llama_index.node_parser import SimpleNodeParser

scripts = SimpleDirectoryReader('..\Raw Transcripts').load_data()

parser = SimpleNodeParser()

nodes = parser.get_nodes_from_documents(scripts)

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="gpt-3.5-turbo"))

max_input_size = 4096

num_output = 300

max_chunk_overlap = 3

prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)