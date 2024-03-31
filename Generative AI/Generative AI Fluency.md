https://develop.deloitte.com/generative-ai-fluency <br>
https://resources.deloitte.com/sites/global/Services/generative-ai/Pages/Generative-AI-Dossier.aspx
https://resources.deloitte.com/sites/global/Services/generative-ai/Pages/Generative-AI-Demo-Videos.aspx

### Gen AI Jumpstart
* Definition: A type of AI that creates original content across various modalities (e.g. text, images, audio, code, etc.) that would have previously taken human skill and expertise to create
* AI --> DS --> ML --> DL --> Gen AI
* Foundation Models
* LLM: Large Language Models
* Prompt Engineering
* Use Cases
  * Content Generation
  * Question Answering
  * Translation
  * Personalized Avatars
  * Document Summarization
  * Named Entity Recognition
 
* Proof of Concept (PoC)
  * It is a demonstration or evidence showing the feasibility or practicality of a particular idea, concept, or project. It is a way to validate that a certain concept or approach can be successfully implemented and will peroform as intended. The primary purpose of a PoC is to assess whether the proposed solution or innovation is technically viable and can meet the specified requirements.

### Gen AI Fluency Part 1 - Welcome to Gen AI
* Five components of GenAI
  * Hardware
    * GPUs, TPUs
  * Cloud Infrastructure
    * AWS, Azure, Google Cloud, Databricks, Snowflake, BigQuery
  * Training Data
    * Image Data - LAION-5B dataset with over 5 million images and associated captions
    * Text Data - books, code, academic writing, medical documents, subtitles, and Wiki
  * Foundation Models
    * NLP: GPT, LLAMA, H3, Transformer XL, BRET
    * Audio: Whisper
    * CV: Florence, SAM, DALL-E, Stable Diffusion
    * Code: Codex
    * Model Training
      * Traditional model - predicts the answer for the new unseen document out of list of known classes
      * Foundation model - uses the first half of the document to predict the second half of the document
  * Fine-tuned Models
  * Applications/Life Cycle of a project

### Gen AI Fluency Part 2 - Generative NLP and CV - A Deeper Look
* Neural Network Models
  * Overall
    * Input layer, hidden layer, output layer
    * parameters - actual numbers, weights
  * CNN - image processing
  * Transformer - sequential data, language translation, text classification, summarization, speech recognition, time series forecasting
  * RNN - NLP, speech recognition, time series forecasting, sentiment analysis, and music generation
  * GNN (Generative Adversarial Networks) - image, transformer
* Natural Language Processing
* Computer Vision
  * Use AI and CS to enable computers to interpret and understand visual information, such as image processing, pattern recognition, object detection, image segmentation, feature extraction, 3D reconstruction, scene understanding, etc.
  * Examples: Generation, Style Transfer, Image Enhancement
  * Diffusion Models: a mathematical model used to explain and predict the spread of info, behavior, or phenomena through a population over time. It is trained to generate a denoised or realistic image from a noisy starting image.
 
### Gen AI Fluency Part 3 - Generative AI and Beyond
* Risks
  * Fairness - AI reflects human biases
  * Privacy & IP - web-scraped datasets may reveal private data, in addition to IP concerns
  * Incorrect & Harmful - incorrect, misleading, or harmful outcomes
 
 * Limitations
   * Ignorance - models rely on training data, limited knowledge
   * Compute - hardware limitations and high costs
   * Intent - models are statistical and lack intentionality, some concepts can be easily imsinterpreted by 1) understanding humor, 2) detecting sarcasm, and 3) responding to emotional language

### Prompt Engineering
https://github.com/brexhq/prompt-engineering <br/>
* Definition: the porcess of designing and refining natural language text prompts - or inputs (e.g. questions) - for use with GenAI models by selecting input formats and relevant data, and fine-tuning language and structure to produce desired outputs (i.e. its responses)
* Prompt engineering is like the source code that a language model interprets
* Terms
  * Temperature: Temperature is a parameter in text generation models that controls the randomness of the output, with lower values producing more focused responses and higher values leading to more diverse, creative outputs.
  * Zero-Shot
    * a setting where zero-labeled data is used in model training or inference
    * refers to teaching a model to do something it has not been explicityly trained to do
  * Few-Shot
    * a setting where the system is given only a very small number of supervised examples
  * Text classification: topic labeling, sentiment analysis, named entity recognition, and natural language inference
  * Text generation: translation, text summarization, and open-domain question answering
* Designing the Prompt (Prompt Engineering)
* Prompt Component
  * Content
  * Expert Persona
  * Task
  * Output <br/>
[C]ontext: As a project manager in a digital marketing agency, [T]ask: could you provide a detailed plan on how to execute a successful social media campaign for a new product launch? [E]xpert Persona: Your expertise in creating engaging content, identifying the right platforms and understanding analytics to measure success should be evident in the plan. [O]utput: This plan should include key tasks, recommended platforms, content creation strategies, scheduling and performance tracking methods."
