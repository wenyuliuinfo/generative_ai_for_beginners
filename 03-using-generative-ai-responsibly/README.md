# Using Generative AI Responsibly
It's easy to be fascinated with AI and generative AI in particular, but you need to consider how you would use it responsibly. You need to consider things like how to ensure the output is fair, non-harmful and more. This chapter aims to provide you with the mentioned context, what to consider, and how to take active steps to improve your AI usage.

**Content**
- [Why Should You Prioritize Responsible AI](#why-should-you-prioritize-responsible-ai)
- [How to Use Generative AI Responsibly](#how-to-use-generative-ai-responsibly)



## Why Should You Prioritize Responsible AI
When building a product, taking a human-centric approach by keeping your user's best interest in mind leads to the best results.

The uniqueness of Generative AI is its power to create helpful answers, information, guidance, and content for users. This can be done without many manual steps which can lead to very impressive results. Without proper planning and strategies, it can also unfortunately lead to some harmful results for your users, your product, and society as a whole.


### 1. Hallucinations
Hallucinations are a term used to describe when an LLM produces content that is either completely nonsensical or something we know is factually wrong based on other sources of information.

The example is a very confident and thorough answer. Unfortunately, it is incorrect. Even with the minimal amount of research, one would discover there was more than one survivor of the Titanic disaster. For a student who is just starting to research this topic, this answer can be persuasive enough to not be questioned and treated as fact. The consequences of this can lead to the AI system being unreliable and negatively impact the reputation of our startup.

With each iteration of any given LLM, we have seen performance improvements around minimizing hallucinations. Even with this improvement, we as application builders and users still need to remain aware of these limitations.


### 2. Harmful Content
We covered in the earlier section when an LLM produces incorrect or nonsensical responses. Another risk we need to be aware of is when a model responds with harmful content.

Harmful content can be defined as:
- Providing instructions or encouraging self-harm or harm to certain groups
- Hateful or demeaning content
- Guiding the planning of any type of attack or violent acts
- Providing instructions on how to find illegal content or commit illegal acts
- Displaying sexually explicit content


### 3. Lack of Fairness
Fairness is defined as "ensuring that an AI system is free from bias and discrimination and that they treat everyone fairly and equally." In the world of Generative AI, we want to ensure that exclusionary worldviews of marginalized groups are not reinforced by the model's output.

These types of outputs are not only destructive to building positive product experiences for our users, but they also cause further societal harm. As application builders, we should always keep a wide and diverse user base in mind when building solutions with Generative AI.



## How to Use Generative AI Responsibly
Now that we have identified the importance of Responsible Generative AI, let's look at 4 steps we can take to build our AI solution responsibly.

![Four_steps](/03-using-generative-ai-responsibly/images/Screenshot%202026-05-20%20at%2010.32.39 AM.png)


### Measure Potential Harms
In software testing, we test the expected actions of a user on an application. Similarly, testing a diverse set of prompts users are most likely going to use is a good way to measure potential harm.


### Mitigate Potential Harms
It is now time to find ways where we can prevent or limit the potential harm caused by the model and its response.
- **Model**. Choosing the right model for the right use case. Larger and more complex models like GPT-4 can cause more of a risk of harmful content when applied to smaller and more specific use cases. Using your training data to fine-tune also reduces the risk of harmful content.
- **Safety System**. A safety system is a set of tools and configurations on the platform serving the model that help mitigate harm. Systems should also detect jailbreak attacks and unwanted activity like requests from bots.
- **Metaprompt**. Metaprompts and grounding are ways we can direct or limit the model based on certain behaviors and information. This could be using system inputs to define certain limits of the model. In addition, providing outputs that are more relevant to the scope or domain of the system.
- **User Experience**. The final layer is where the user interacts directly with the model through our application's interface in some way. In this way we can design the UI/UX to limit the user on the types of inputs they can send to the model as well as text or images displayed to the user. When deploying the AI application, we also must be transparent about what our Generative AI application can and can't do.
- **Evaluate model**. Working with LLMs can be challenging because we don't always have control over the data the model was trained on. Regardless, we should always evaluate the model's performance and outputs. It's still important to measure the model's accuracy, similarity, groundedness, and relevance of the output. This helps provide transparency and trust to stakeholders and users.


### Operate a Responsible Generative AI Solution
Building an operational practice around your AI applications is the final stage. This includes partnering with other parts of our startup like Legal and Security to ensure we are compliant with all regulatory policies. Before launching, we also want to build plans around delivery, handling incidents, and rollback to prevent any harm to our users from growing.