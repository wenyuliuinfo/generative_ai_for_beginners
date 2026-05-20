# Building a Search Applications
There's more to LLMs than chatbots and text generation. It's also possible to build search applications using Embeddings. Embeddings are numerical representations of data also known as vectors, and can be used for semantic search for data.

**Content**
- [Why build a search application](#why-build-a-search-application)
- [What is semantic search](#what-is-semantic-search)
- [What are text embeddings](#what-are-text-embeddings)
- [How is the embedding index created](#how-is-the-embedding-index-created)
- [Understanding cosine similarity](#understanding-cosine-similarity)



## Why build a search application?
Creating a search application will help you understand how to use Embeddings to search for data. You will also learn how to build a search application that can be used by students to find information quickly.

The lesson includes an Embedding Index of the YouTube transcripts for the Microsoft AI Show YouTube channel. The AI Show is a YouTube channel that teaches you about AI and machine learning. The Embedding Index contains the Embeddings for each of the YouTube transcripts up until Oct 2023. You will use the Embedding Index to build a search application for our startup.



## What is semantic search?
Now you might be wondering, what is semantic search? Semantic search is a search technique that uses the semantics, or meaning, of the words in a query to return relevant results.

Here is an example of a semantic search. Let's say you were looking to buy a car, you might search for "my dream car", semantic search understands that you are not `dreaming` about a car, but rather you are looking to buy your `ideal` car. Semantic search understands your intention and returns relevant results.



## What are text embeddings?
Text embeddings are a text representation technique used in natural language processing. Text embeddings are semantic numerical representations of text. Embeddings are used to represent data in a way that is easy for a machine to understand. There are many models for building text embeddings, in this lesson, we will focus on generating embeddings using the OpenAI Embedding Model.

Here's an example, imagine the following text is in a transcript from one of the episodes on the AI Show YouTube channel:
```
Today we are going to learn about Azure Machine Learning.
```

We'd pass the text to the OpenAI Embedding API and it would return the following embedding consisting of 1536 numbers aka a vector. Each number in the vector represents a different aspect of the text. For brevity, here are the first 10 numbers in the vector.
```
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```


## How is the embedding index created?
The embedding index for this lesson was created with a series of Python scripts. You will find the scripts along with instructions in the "scripts" folder. You don't need to run these scripts to complete this lesson as the embedding index is provided.

The scripts perform the following operations:
1. The transcript for each YouTube video in the AI Show playlist is downloaded.
2. Using OpenAI Functions, an attempt is made to extract the speaker name form the first 3 minutes of the YouTube transcript. The speaker name for each video is stored in the embedding index named `embedding_index_3m.json`.
3. The transcript text is then chunked into 3 minute text segments. The segment includes about 20 words overlapping from the next segment to ensure that the embedding for the segment is not cut off and to provide better search context.
4. Each text segment is then passed to the OpenAI Chat API to summarize the text into 60 words. The summary is also stored in the embedding index `embedding_index_3m.json`.
5. Finally, the segment text is passed to the OpenAI embedding API. The embedding API returns a vector of 1536 numbers that represent the semantic meaning of the segment. The segment along with the OpenAI embedding vector is stored in an embedding index `embedding_index_3m.json`.

### Vector Databases
For lesson simplicity, the embedding index is stored in a JSON file named `embedding_index_3m.json` and loaded into a Pandas DataFrame. However, in production, the embedding index would be stored in a vector database such as Azure Cognitive Search, Redis, Pinecone, Weaviate and so on.



## Understanding cosine similarity
We've learned about text embeddings, the next step is to learn how to use text embeddings to search for data and in particular find the most similar embeddings to a given query using cosine similarity.

### What is cosine similarity?
Cosine similarity is a measure of similarity between two vectors, you'll also hear this referred to as `nearest neighbor search`. To perform a cosine similarity search you need to vectorize for query text using the OpenAI Embedding API. Then calculate the cosine similarity between the query vector and each vector in the embedding index. Remember, the embedding index has a vector for each YouTube transcript text segment. Finally, sort the results by cosine similarity and the text segments with the highest cosine similarity are the most similar to the query.

From a mathematic perspective, cosine similarity measures the cosine of the angle between two vectors projected in a multidimensional space. This measurement is beneficial, because if two documents are far apart by Euclidean distance because of size, they could still have a smaller angle between them and therefore higher cosine similarity.