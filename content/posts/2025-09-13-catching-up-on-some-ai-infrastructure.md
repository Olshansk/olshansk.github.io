---
title: "Catching up on some ai infrastructure"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: ["Post"]
categories: []
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

#TIL I caught up on a handful of cool things in the world LLM enabling infrastructure.

https://abishekmuthian.com/how-i-run-llms-locally/?utm_source=tldrnewsletter

## **What do I pay for?**

  * Only refers to LLM Developer tooling, not products

  * ChatGPT Pro

  * Claude Pro

  * Before you bring it up, I don’t pay for things like Supermaven, cursor, etc…




## **Cursor**

  * Building the muscle to help with refactor

  * The moment I feel my brain stop working, I try to see if AI can do it

  * It’s akin to renaming things in the past 




## **Cursor / RAG Pipeline**

## **Ollama**

  * **Website** : Their [models directory](https://ollama.com/search)

  * **Interface** : a




## **Cerebras**

  1. **Supabase**



  1. **HugingFace**



  1. **OpenRouter**



  1. Grok/x




## **AI Gateways**

  * <https://konghq.com/products/kong-ai-gateway>

  * <https://portkey.ai/features/ai-gateway>

  * 

  1. **Ollama** is still the easiest way to run models locally. It’s easy. Their UI is on point. It’s hard to believe how great of a product this is. [1]

  2. **Cerebras** inference really is ULTRA fast. I don’t need anything this fast, but I appreciate someone is building it.

     1. They’re public about how they do this using CS-3. If you’re in software (like me), this is what real engineering looks like [2]

     2. Their main README is just one page with all the APIs you’ll need. Best of all, they’re all OpenAI compatible. [3]

     3. They have the best (short & to the point) example of RAG using docker + pinecone (my go-to stack). [4]

  3. **Supabase** released **[database.build](http://database.build/)** which lets you explain the idea you need and they build the schema for you. Then you can deploy the database with the click of a button. Amazing!!! [5]

     1. The full blog post is full of juicy details [6]

     2. PGLite enables running a full Postgres database locally (in the browser) using WASM that is both reactive and syncs live [7]

     3. Electric is like GraphQL but for Postgres. It has an HTTP API that lets you query Postgres “shapes”.

  4. **Hugginface** has direct integration with ollama. It doesn’t work for every model out of the box, but for some, you can just run one command and it’s available locally:




```

ollama run [hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:IQ4_XS](http://hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:IQ4_XS)

```

https://huggingface.co/docs/hub/en/ollama

  1. **Postgres** has a lot of AI related extensions




[6] <https://github.com/Olshansk/postgres_for_everything>

  1. **OpenRouter.AI** has two login options: Google & MetaMask. Interesting…



  1. 


## **Uncensored Models**

  * https://huggingface.co/Guilherme34/Llama-3.2-11b-vision-uncensored/discussions/3



  * The benefit of open source is to have access to uncensored models

  * The truth is:

    * We use whatever is off the shelf

    * They’re harder to use

    * They’re harder to find

    *   * 


## **Pydantic AI**

  * **Good idea** : https://www.anthropic.com/news/model-context-protocol

  * **Good execution** : https://ai.pydantic.dev/models/#environment-variable




https://ollama.com/

[2] <https://cerebras.ai/product-system/>

[3] <https://github.com/Cerebras/cerebras-cloud-sdk-python>

[4] <https://github.com/Cerebras/inference-examples/tree/main/rag-pinecone-docker>

[5] 

https://database.build/

[6] <https://supabase.com/blog/database-build-v2>

[7] https://pglite.dev/

[8] 

https://electric-sql.com/

[5] <https://huggingface.co/docs/hub/en/ollama>

[7] <https://platform.openai.com/docs/examples>

[9] 

https://openrouter.ai/

Publish all of the above in notes: https://olshansky.substack.com/notes
