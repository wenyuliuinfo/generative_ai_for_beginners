# Exploring and Comparing Different LLMs

With the previous lesson, we have seen how Generative AI is changing the technology landscape, how Large Language Models (LLMs) work and how a business can apply them to their use cases and grow. In this chapter, we're looking to compare and contrast different types of Large Language Models (LLMs) to understand their pros and cons.

**Content**

- [Understand Different Types of LLMs](#understand-different-types-of-llms)
- [Improving LLM Results](#improving-llm-results)


## Understand Different Types of LLMs
LLMs can have multiple categorizations based on their architecture, training data, and use case. Understanding these differences will help our startup select the right model for the scenario, and understand how to test, iterate, and improve performance.

There are many different types of LLM models, your choice of model depends on what you aim to use them for, your data, how much you're ready to pay and more.

Depending on if you aim to use the models for text, audio, video, image generation and so on, you might opt for a different type of model.
- **Audio and speech recognition**: For this purpose, Whisper-type models are a great choice as they-re general-purpose and aimed at speech recognition. It's trained on diverse audio and can perform multilingual speech recognition.
- **Image Generation**: For image generation, DALL-E and Midjourney are two very well-known choices.
- **Text Generation**: Most models are trained on text generation and you have a large variety of choices from GPT-3.5 to GPT-4. They come at different costs.
- **Multi-modality**: If you're looking to handle multiple types of data in input and output, you might want to look into models gpt-4 turbo with vision or gpt-4o - the latest releases of OpenAI models - which are capable to combine natural language processing to visual understanding, enabling interactions through multi-modal interfaces.

Selecting a model means you get some basic capabilities, that might not be enough. Often you have company specific data that you somehow need to tell the LLM about. 


### Foundation Models vs. LLMs
The term Foundation Model was coined by Stanford researchers and defined as an AI model that follows some criteria, such as:
- **They are trained using unsupervised learning or self-supervised learning**, meaning they are trained on unlabeled multi-modal data, and they do not require human annotation or labeling of data for their training process.
- **They are very large models**, based on very deep neural networks trained on billions of parameters.
- **They are normally intended to serve as a foundation for other models**, meaning they can be used as starting point for other models to be built on top of, which can be done by fine-tuning.

![Foundation_Models](/02-exploring-and-comparing-different-llms/images/Screenshot%202026-05-20%20at%209.01.20 AM.png)

To further clarify this distinction, let's take ChatGPT as an example. To build the first version of ChatGPT, a model called GPT-3.5 served as the foundation model. This means that OpenAI used some chat-specific data to create a tuned version of GPT-3.5 that was specialized in performing well in conversational scenarios, such as chatbots.


### Open Source vs. Proprietary Models
Another way to categorize LLMs is whether they are open source or proprietary.

Open-source models are models that are made available to the public and can be used by anyone. They are often made available by the company that created them, or by the research community. These models are allowed to be inspected, modified, and customized for the various use cases in LLMs. However, they are not always optimized for production use, and may not be as performant as proprietary models. Plus, funding for open-source models can be limited, and they may not be maintained long term or may not be updated with the latest research.

Proprietary models are models that are owned by a company and are not made available to the public. These models are often optimized for production use. However, they are not allowed to be inspected, modified, or customized for different use cases. Plus, they are not always available for free, and may require a subscription or payment to use. Also, users do not have control over the data that is used to train the model, which means they should entrust the model owner with ensuring commitment to data privacy and responsible use of AI.


### Embedding vs. Image Generation vs. Text and Code Generation
LLMs can also be categorized by the output they generate.

**Embeddings** are a set of models that can convert text into a numerical form, called embedding, which is a numerical representation of the input text. Embeddings make it easier for machines to understand the relationships between words or sentences and can be consumed as inputs by other models, such as classification models, or clustering models that have better performance on numerical data. Embedding models are often used for transfer learning, where a model is built for a surrogate task for which there's an abundance of data, and then the model weights are re-used for other downstream tasks. An example is OpenAI embeddings.

[!Embeddings](/02-exploring-and-comparing-different-llms/images/Screenshot%202026-05-20%20at%209.14.11 AM.png)

**Image generation** models are models that generate images. These models are often used for image editing, image synthesis, and image translation. Image generation models are often trained on large datasets of images, such as LAION-5B, and can be used to generate new images or to edit existing images with inpainting, super-resolution, and colorization techniques. Examples include DALL-E-3 and Stable Diffusion models.

[!Image_generation](/02-exploring-and-comparing-different-llms/images/Screenshot%202026-05-20%20at%209.17.25 AM.png)

**Text and code generation** models are models that generate text or code. These models are often used for text summarization, translation, and question answering. Text generation models are often trained on large datasets of text, such as BookCorpus, and can be used to generate new text, or to answer questions. Code generation models, like CodeParrot, are often trained on large datasets of code, such as GitHub, and can be used to generate new code, or to fix bugs in existing code.


### Encoder-Decoder vs. Decoder-only
To talk about the different types of architecture of LLMs, let's use an analogy.

Imagine your manager gave you a task for writing a quiz for students. You have two colleagues; one oversees creating the content and the other oversees reviewing them.

The content creator is like a Decoder only model, they can look at the topic and see what you already wrote and then can write a course based on that. They are very good at writing engaging and informative content, but they are not very good at understanding the topic and the learning objectives. Some examples of Decoder models are GPT family models, such as GPT-3.

The reviewer is like an Encoder only model, they look at the course written and answers, noticing the relationship between them and understanding context, but they are not good at generating content. An example of Encoder only model would be BERT.

Imagine that we can have someone as well who could create and review the quiz, this is an Encoder-Decoder model. Some examples would be BART and T5.


### Service vs. Model
A service is a product that is offered by a Cloud Service Provider, and is often a combination of models, data, and other components. A model is the core component of a service, and is often a foundation model, such as an LLM.

Services are often optimized for production use and are often easier to use than models, via a graphical user interface.

Models are just the Neural Network, with the parameters, weights, and others. Allowing companies to run locally, however, would need to buy equipment, build a structure to scale and buy a license or use an open-source model. A model like LLaMA is available to be used, requiring computational power to run the model.



## Improving LLM Results
We've explored with our startup team different kinds of LLMs and a Cloud Platform enabling us to compare different models, evaluate them on test data, improve performance and deploy them on inference endpoints.

But when shall they consider fine-tuning a model rather than using a pre-trained one? Are there other approaches to improve model performance on specific workloads?

There are several approaches a business can use to get the results they need from an LLM. You can select different types of models with different degrees of training when deploying an LLM in production, with different levels of complexity, cost, and quality. Here are some different approaches:
- **Prompt engineering with context**. The idea is to provide enough context when you prompt to ensure you get the response you need.
- **Retrieval Augmented Generation, RAG**. Your data might exist in a database or web endpoint for example, to ensure this data, or a subset of it, is included at the time of prompting, you can fetch the relevant data and make that part of the user's prompt.
- **Fine-tuned Model**. Here, you trained the model further on your own data which led to the model being more exact and responsive to your needs but might be costly.

[!Four_ways_deploy_llms](/02-exploring-and-comparing-different-llms/images/Screenshot%202026-05-20%20at%209.40.04 AM.png)


### 1. Prompt Engineering with Context
Pre-trained LLMs work very well on generalized natural language tasks, even by calling them with a short prompt, like a sentence to complete or a question.

However, the more the user can frame their query, with a detailed request and examples - the context -  the more accurate and closest to user's expectations the answer will be. In this case, we talk about if the prompt includes only one example and if it includes multiple examples. Prompt engineering with context is the most cost-effective approach to start with.


### 2. Retrieval Augmented Generation (RAG)
LLMs have the limitation that they can use only the data that has been used during their training to generate an answer. This means that they don't know anything about the facts that happened after their training process, and they cannot access non-public information. This can be overcome through RAG, a technique that augments prompt with external data in the form of chunks of documents, considering prompt length limits. This is supported by Vector database tools that retrieve the useful chunks from varied pre-defined data sources and add them to the prompt context.

This technique is very helpful when a business doesn't have enough data, enough time, or resources to fine-tune an LLM, but still wishes to improve performance on a specific workload and reduce risks of fabrications.


### 3. Fine-tuned Model
Fine-tuning is a process that leverages transfer learning to adapt the model to a downstream task or to solve a specific problem. Differently from prompt learning and RAG, it results in a new model being generated, with updated weights and biases. It requires a set of training examples consisting of a single input and its associated output. This would be the preferred approach if:
- **Using fine-tuned models**. A business would like to use fine-tuned less capable models rather than high performance models, resulting in a more cost effective and fast solution.
- **Considering latency**. Latency is important for a specific use-case, so it's not possible to use very long prompts or the number of examples that should be learned from the model doesn't fit with the prompt length limit.
- **Staying up to date**. A business has a lot of high-quality data and ground truth labels and the resources required to maintain this data up to date over time.


### 4. Trained Model
Training an LLM from scratch is without a doubt the most difficult and the most complex approach to adopt, requiring massive amounts of data, skilled resources, and appropriate computational power. This option should be considered only in a scenario where a business has a domain-specific use case and a large amount of domain-centric data.
