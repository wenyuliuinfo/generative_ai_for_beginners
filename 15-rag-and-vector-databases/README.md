# Retrieval Augmented Generation (RAG) and Vector Databases

In the search applications lesson, we briefly learned how to integrate your own data into LLM. In this lesson, we will delve further into the concepts of grounding your data in your LLM application, the mechanics of the process and the methods for storing data, including both embeddings and text.

**Content**
- [Scenario: Enhancing our LLMs with our own data](#scenario-enhancing-our-llms-with-our-own-data)
- [Retrieval Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
- [Creating a knowledge base](#creating-a-knowledge-base)
- [Retrieval and vector search](#retrieval-and-vector-search)


## Scenario: Enhancing our LLMs with our own data
For this lesson, we want to add our own notes into the education startup, which allows the chatbot to get more information on the different subjects. Using the notes that we have, learners will be able to study better and understand the different topics, making it easier to revise for their examinations. To create our scenario, we will use:
- `Azure OpenAI`: the LLM we will use to create our chatbot
- `AI for beginners' lesson on Neural Networks`: this will be the data we ground our LLM on


## Retrieval Augmented Generation (RAG)
An LLM powered chatbot processes user prompts to generate responses. It is designed to be interactive and engages with user on a wide array of topics. However, its responses are limited to the context provided and its foundational training data. For instance, GPT-4 knowledge cutoff is Sep 2021, meaning, it lacks knowledge of events that have occurred after this period. In addition, the data used to train LLMs excludes confidential information such as personal notes or a company's product manual.

### How RAGs Work

![RAG_work](/15-rag-and-vector-databases/images/Screenshot%202026-05-23%20at%207.45.05 AM.png)

Suppose you want to deploy a chatbot that creates quizzes from your notes, you will require a connection to the knowledge base. This is where RAG comes to rescue. RAGs operate as follows:
- **Knowledge base**: Before retrieval, these documents need to be ingested and preprocesses, typically breaking down large documents into smaller chunks, transforming them to text embedding and storing them in a database.
- **User Query**: the user asks a question.
- **Retrieval**: When a user asks a question, the embedding model retrieves relevant information from our knowledge base to provide more context that will be incorporated into the prompt.
- **Augmented Generation**: the LLM enhances its response based on the data retrieved. It allows the response generated to be not only based on pre-trained data but also relevant information from the added context. The retrieved data is used to augment the LLM's responses. The LLM then returns an answer to the user's question.

![encoder_decoder](/15-rag-and-vector-databases/images/Screenshot%202026-05-23%20at%207.52.21 AM.png)

The architecture for RAGs is implemented using transformers consisting of two parts: an encoder and a decoder. For example, when a user asks a question, the input text "encoded" into vectors capturing the meaning of words and the vectors are "decoded" into our document index and generates new text based on the user query. The LLM uses both an encoder-decoder model to generate the output.

Two approaches when implementing RAG:
- **RAG-Sequence** using retrieved documents to predict the best possible answer to a user query.
- **RAG-Token** using documents to generate the next token, then retrieve them to answer the user's query.

### Why would you use RAGs?
Information richness: ensures text responses are up to date and current. It enhances performance on domain specific tasks by accessing the internal knowledge base.

Reduces fabrication by utilizing verifiable data in the knowledge base to provide context to the user queries.

It is cost effective as they are more economical compared to fine-tuning an LLM.



## Creating a Knowledge Base
Our application is based on our personal data, i.e., the Neural Network lesson on AI for Beginners curriculum.

### Vector Database
A vector database, unlike traditional database, is a specialized database designed to store, manage and search embedded vectors. It stores numerical representations of documents. Breaking down data to numerical embeddings makes it easier for our AI system to understand and process the data.

We store our embeddings in vector databases as LLMs have a limit of the number of tokens they accept as input. As you cannot pass the entire embeddings to an LLM, we will need to break them down into chunks and when a user asks a question, the embeddings most like the question will be returned together with the prompt. Chunking also reduces costs on the number of tokens passed through an LLM.

Some popular vector databases include Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant and DeepLake.

You can create a Pinecone emulator using the following docker image:
```bash
docker run -d \
  --name pinecone-local \
  -e PORT=5080 \
  -e PINECONE_HOST=localhost \
  -p 5080-5090:5080-5090 \
  --platform linux/amd64 \
  ghcr.io/pinecone-io/pinecone-local:latest
```

### From Text to Embeddings
Before we store our data, we will need to convert it to vector embeddings before it is stored in the database. If you are working with large documents or long texts, you can chunk them based on queries you expect. Chunking can be done at sentence level, or at a paragraph level. As chunking derives meanings from the words around them, you can add some other context to a chunk, for example, by adding the document title or including some text before or after the chunk. You can chunk the data as follows:

```python
def split_text(text, max_len, min_len):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_len and len(' '.join(current_chunk)) > min_len:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks
```

Once chunked, we can then embed our text using different embedding models. Some models you can use include: word2vec, ada-002 by OpenAI and many more. Selecting a model to use will depend on the languages you're using, the type of content encoded, the size of input it can encode and length of the embedding output.


## Retrieval and Vector Search
When a user asks a question, the retriever transforms it into a vector using the query encoder, it then searches through our document search index for relevant vectors in the document that are related to the input. Once done, it converts both the input vector and document vectors into text and passes it through the LLM.

### Retrieval
Retrieval happens when the system tries to quickly find the documents from the index that satisfy the search criteria. The goal of the retriever is to get documents that will be used to provide context and ground the LLM on your data.

There are several ways to perform search within our database such as:
- **Keyword search**: used for text searches.
- **Vector search**: converts documents from text to vector representations using embedding models, permitting a semantic search using the meaning of words. Retrieval will be done by querying the documents whose vector representations are closest to the user question.
- **Hybrid**: a combination of both keyword and vector search.

### Vector Similarity
The retriever will search through the knowledge database for embeddings that are close together, the closest neighbour, as they are texts that are similar. In the scenario a user asks a query, it is first embedded them matched with similar embeddings. The common measurement that is used to find how similar different vectors are is cosine similarity which is based on the angle between two vectors.

### Search Index
When doing retrieval, we will need to build a search index for our knowledge base before we perform search. An index will store our embeddings and can quickly retrieve the most similar chunks even in a large database.

### Re-ranking
Once you have queried the database, you might need to sort the results from the most relevant. A re-ranking LLM utilizes Machine Learning to improve the relevance of search results by ordering them from the most relevant. 
