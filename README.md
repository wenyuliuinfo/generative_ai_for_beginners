# Generative AI for Beginners

This repository is a practical, code-first adaptation of Microsoft's excellent "[Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)" course. It is designed to provide a hands-on, coding-centric learning path for developers who want to move beyond theory and start building real-world generative AI applications.

## 🎯 About This Repository

The goal of this repo is to distill the core concepts of the original Microsoft course into executable Jupyter Notebook examples and Python scripts. It emphasizes practical implementation, allowing you to learn by building applications that leverage Large Language Models (LLMs), prompt engineering, vector databases, and more.

This is a project-based learning resource for developers, data scientists, and AI enthusiasts who want to quickly get started with the practical aspects of Generative AI.

## 📂 Repository Structure

The content is organized to follow a logical learning journey, mirroring and expanding upon the structure of the original course with a focus on code.

```
generative_ai_for_beginners/
├── 01-intro-to-genai/                          # Introduction to Generative AI concepts
├── 02-exploring-and-comparing-different-llms/  # LLM landscape and comparison
├── 03-using-generative-ai-responsibly/         # Ethical considerations and responsible AI
├── 04-prompt-engineering-fundamentals/         # Core techniques for effective prompting
├── 06-text-generation-apps/                    # Building applications for text generation
├── 08-building-search-applications/            # Creating search apps with LLMs
├── 09-building-image-applications/             # Applications for image generation and analysis
├── 11-integrating-with-function-calling/       # Enabling LLMs to call external functions
├── 12-designing-ux-for-ai-applications/        # UX best practices for AI-powered apps
├── 13-securing-ai-applications/                # Security considerations for Gen AI
├── 14-generative-ai-application-lifecycle/     # The full lifecycle of a Gen AI project
├── 15-rag-and-vector-databases/                # Retrieval-Augmented Generation (RAG) & Vector DBs
├── .gitignore
└── README.md
```

Each lesson folder typically contains:
*   **`README.md`**: A guide to the lesson's objectives and concepts.
*   **`.ipynb` Jupyter Notebooks**: Interactive code examples to run and experiment with.
*   **`.py` Python scripts**: More structured code for applications and utilities.

## 🚀 Getting Started

### Prerequisites
To effectively use this repository, you should have:
*   Basic knowledge of Python.
*   An understanding of fundamental machine learning concepts (helpful, but not strictly required).
*   A code editor (like VS Code) or a Jupyter environment.

### Installation & Running the Code

1. **Clone the repository:**
    ```bash
    git clone https://github.com/wenyuliuinfo/generative_ai_for_beginners.git
    cd generative_ai_for_beginners/<lesson_folder_name>/python/
    ```

2. **Set up a Python environment:**
It's highly recommended to use a virtual environment. You can use venv.
    ```bash
    # Using venv (Python 3.8+)
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
(Note: If a requirements.txt file is not present in the root, you may need to install libraries like `openai`, `chromadb`, `pillow`, `numpy`, `pandas` individually as needed for each lesson.)

4. **Set up your API Keys:**
Many lessons require an API key from an LLM provider (e.g., DeepSeek, OpenAI, Azure OpenAI, or a local model). Create a .env file in the root directory and add your keys:
    ```text
    OPENAI_API_KEY="your-api-key-here"
    DEEPSEEK_API_KEY="your-api-key-here"
    DEEPSEEK_BASE_URL="your-api-url-here"
    ```

5. **Launch Jupyter:**
Navigate to a lesson folder and start Jupyter Notebook or Jupyter Lab.
    ```bash
    jupyter notebook
    ```

## 🧠 Key Topics Covered

This repository will guide you through the essential components of modern Generative AI development:

- **LLM Fundamentals:** Understanding what LLMs are, their capabilities, and how to choose between different models.
- **Prompt Engineering:** Mastering the art of crafting effective prompts to guide LLM behavior, from zero-shot to few-shot and chain-of-thought prompting.
- **Responsible AI:** Learning about the ethical implications, biases, and safety considerations in deploying Gen AI.
- **Text Generation Applications:** Building practical apps like chatbots, creative writing tools, and content generators.
- **Search Applications:** Creating applications that use embeddings and semantic search to find relevant information.
- **Image Applications:** Working with multimodal models to generate and analyze images.
- **Function Calling:** Enabling LLMs to interact with external APIs and tools to perform actions.
- **User Experience (UX):** Designing intuitive and effective user interfaces for AI applications.
- **Security:** Implementing best practices to secure your AI applications and data.
- **Application Lifecycle:** Understanding the end-to-end process from development to deployment.
- **Retrieval-Augmented Generation (RAG) & Vector Databases:** A deep dive into RAG, a crucial technique for grounding LLMs in proprietary or up-to-date data. You'll learn to work with vector databases (like Chroma, Pinecone) to build knowledge-aware applications.