# Securing Your Generative AI Applications

**Content**
- [What does security mean within the context of generative AI](#what-does-security-mean-within-the-context-of-generative-ai)
- [Understanding the threats and risks of AI](#understanding-the-threats-and-risks-of-ai)
- [Security testing for AI systems and LLMs](#security-testing-for-ai-systems-and-llms)


## What does security mean within the context of Generative AI?
As AI and ML technologies increasingly shape our lives, it's crucial to protect not only customer data but also the AI systems themselves. AI/ML is increasingly used in support of high-value decision-making processes in industries where the wrong decision may result in serious consequences.

Here are key points to consider:
- **Impact of AI/ML**: AI/ML have significant impacts on daily life and as such safeguarding them has become essential.
- **Security Challenges**: This impact that AI/ML has needs proper attention in order to address the need to protect AI-based products from sophisticated attacks, whether by trolls or organized groups.
- **Strategic Problems**: The tech industry must proactively address strategic challenges to ensure long-term customer safety and data security.

Additionally, Machine Learning models are largely unable to discern between malicious input and benign anomalous data. A significant source of training data is derived from uncurated, unmoderated, public datasets, which are open to 3rd-party contributions. Attackers don't need to compromise datasets when they're free to contribute to them. Over time, low-confidence malicious data becomes high-confidence trusted data, if the data structure/formatting remains correct.

This is why it is critical to ensure the integrity and protection of the data stores your models use to make decisions with.


## Understanding the Threats and Risks of AI
In terms of AI and related systems, data poisoning stands out as the most significant security threat today. Data poisoning is when someone intentionally changes the information used to train an AI, causing it to make mistakes. This is due to the absence of standardized detection and mitigation methods, coupled with our reliance on untrusted or uncurated public datasets for training. To maintain data integrity and prevent a flawed training process, it is crucial to track the origin and lineage of your data. Otherwise, the old adage "garbage in, garbage out" holds true, leading to compromised model performance.

Here are examples of how data poisoning can affect your models:
1. **Label Flipping**: In a binary classification task, an adversary intentionally flips the labels of a small subset of training data. (Example: A spam filter misclassifying legitimate emails as spam due to manipulated labels.)
2. **Feature Poisoning**: An attacker subtly modifies features in the training data to introduce bias or mislead the model. (Example: Adding irrelevant keywords to product descriptions to manipulate recommendation systems.)
3. **Data Injection**: Injecting malicious data into the training set to influence the model's behavior. (Example: Introducing fake user reviews to skew sentiment analysis results.)
4. **Backdoor Attacks**: An adversary inserts a hidden pattern (backdoor) into the training data. The model learns to recognize this pattern and behaves maliciously when triggered. (Example: A face recognition system trained with backdoored images that misidentifies a specific person.)

The MITRE Corporation has created ATLAS, a knowledge-base of tactics and techniques employed by adversaries in real-world attacks on AI systems.

Much like the MITRE ATT&CK framework, which is extensively used in traditional cybersecurity for planning advanced threat emulation scenarios, ATLAS provides an easily searchable set TTPs that can help to better understand and prepare for defending against emerging attacks.

Additionally, the Open Web Application Security Project (OWASP) has created a "Top 10 list" of the most critical vulnerabilities found in applications utilizing LLMs. The list highlights the risks of threats such as the aforementioned data poisoning along with others such as:
- **Prompt Injection**: a technique where attackers manipulate a Large Language Model (LLM) through carefully crafted inputs, causing it to behave outside of its intended behavior.
- **Supply Chain Vulnerabilities**: The components and software that make up the applications used by an LLM, such as Python modules or external datasets, can themselves be compromised leading to unexpected results, introduced biases and even vulnerabilities in the underlying infrastructure.
- **Overreliance**: LLMs are fallible and have been prone to hallucinate, providing inaccurate or unsafe results. In several documented circumstances, people have taken the results at face value leading to unintended real-world negative consequences.


## Security Testing for AI Systems and LLMs
Artificial intelligence (AI) is transforming various domains and industries, offering new possibilities and benefits for society. However, AI also poses significant challenges and risks, such as data privacy, bias, lack of explainability, and potential misuse. Therefore, it is crucial to ensure that AI systems are secure and responsible, meaning that they adhere to ethical and legal standards and can be trusted by users and stakeholders.

Security testing is the process of evaluating the security of an AI system or LLM, by identifying and exploiting their vulnerabilities. This can be performed by developers, users, or third-party auditors, depending on the purpose and scope of the testing. Some of the most common security testing methods for AI systems and LLMs are:
1. **Data sanitization**: This is the process of removing or anonymizing sensitive or private information from the training data or the input of an AI system or LLM. Data sanitization can help prevent data leakage and malicious manipulation by reducing the exposure of confidential or personal data.
2. **Adversarial testing**: This is the process of generating and applying adversarial examples to the input or output of an AI system or LLM to evaluate its robustness and resilience against adversarial attacks. Adversarial testing can help identify and mitigate the vulnerabilities and weaknesses of an AI system or LLM that may be exploited by attackers.
3. **Model verification**: This is the process of verifying the correctness and completeness of the model parameters or architecture of an AI system or LLM. Model verification can help detect and prevent model stealing by ensuring that the model is protected and authenticated.
4. **Output validation**: This is the process of validation the quality and reliability of the output of an AI system or LLM. Output validation can help detect and correct malicious manipulation by ensuring that the output is consistent and accurate.

### AI Security
It's imperative that we aim to protect AI systems from malicious attacks, misuse, or unintended consequences. This includes taking steps to ensure the safety, reliability, and trustworthiness of AI systems, such as:
- **Securing the data and algorithms** that are used to train and run AI models.
- **Preventing unauthorized access**, manipulation, or sabotage of AI systems.
- **Detecting and mitigating bias**, discrimination, or ethical issues in AI systems.
- **Ensuring the accountability**, transparency, and explainability of AI decisions and actions.
- **Aligning the goals and values** of AI systems with those of humans and society.

### Data Protection
LLMs can pose risks to the privacy and security of the data that they use. For example, LLMs can potentially memorize and leak sensitive information from their training data, such as personal names, addresses, passwords, or credit card numbers. Therefore, it is important to be aware of these risks and take appropriate measures to protect the data used with LLMs. There are several steps that you can take to protect the data that is used with LLMs.
- **Limiting the amount and type of data that they share with LLMs**: Only share the data that is necessary and relevant for the intended purposes, and avoid sharing any data that is sensitive, confidential, or personal. Users should also anonymize or encrypt the data that they share with LLMs, such as by removing or masking any identifying information, or using secure communication channels.
- **Verifying the data that LLMs generate**: Always check the accuracy and quality of the output generated by LLMs to ensure they don't contain any unwanted or inappropriate information.
- **Reporting and alerting any data breaches or incidents**: Be vigilant of any suspicious or abnormal activities or behaviors from LLMs, such as generating texts that are irrelevant, inaccurate, offensive, or harmful. This could be an indication of a data breach or security incident.
  
### Emulating real-world threats - AI Red Teaming
Emulating real-world threats is now considered a standard practice in building resilient AI systems by employing similar tools, tactics, procedures to identify the risks to systems and test the response of defenders.

Below are key insights that have shaped Microsoft's AI Red Team program.
1. **Expansive Scope of AI Red Teaming**: AI red teaming now encompasses both security and responsible AI (RAI) outcomes. Traditionally, red teaming focused on security aspects, treating the model as a vector. However, AI systems introduce novel security vulnerabilities, necessitating special attention. Beyond security, AI red teaming also probes fairness issues and harmful content. Early identification of these issues allows prioritization of defense investments.
2. **Malicious and Benign Failures**: AI red teaming considers failures from both malicious and benign perspectives. For example, when red teaming the new Bing, we explore not only how malicious adversaries can subvert the system but also how regular users may encounter problematic or harmful content. AI red teaming accounts for a broader range of personas and potential failures.
3. **Dynamic Nature of AI Systems**: AI applications constantly evolve. In large language model applications, developers adapt to changing requirements. Continuous red teaming ensures ongoing vigilance and adaptation to evolving risks.


