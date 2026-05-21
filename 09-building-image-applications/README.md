# Building Image Generation Applications
There's more to LLMs than text generation. It's also possible to generate images from text descriptions. Having images as a modality can be highly useful in a number of areas from MedTech, architecture, tourism, game development and more. In this chapter, we will look into the two most popular image generation models, DALL-E and Midjourney.

**Content**
- [Why build an image generation application](#why-build-an-image-generation-application)
- [What is DALL-E and Midjourney](#what-is-dall-e-and-midjourney)
- [How does DALL-E and Midjourney work](#how-does-dall-e-and-midjourney-work)
- [Additional capabilities of image generation](#additional-capabilities-of-image-generation)
- [Temperature](#temperature)


## Why build an image generation application?
Image generation applications are a great way to explore the capabilities of Generative AI. They can be used for:
- **Image editing and synthesis**. You can generate images for a variety of use cases, such as image editing and image synthesis.
- **Applied to a variety of industries**. They can also be used to generate images for a variety of industries like MedTech, Tourism, Game development and more.


## What is DALL-E and Midjourney?
DALL-E and Midjourney are two of the most popular image generation models, they allow you to use prompt to generate images.

### DALL-E
Let's start with DALL-E, which is a Generative AI model that generates images from text descriptions. DALL-E is a combination of two models, CLIP and diffused attention.
- **CLIP**, is a model that generates embeddings, which are numerical representations of data, from images and text.
- **Diffused attention**, is a model that generates images from embeddings. DALL-E is trained on a dataset of images and text and can be used to generate images from text descriptions. For example, DALL-E can be used to generate images of a cat in a hat.

### Midjourney
Midjourney works in a similar way to DALL-E, it generates images from text prompts. Midjourney can also be used to generate images using prompts like "a cat in a hat".


## How does DALL-E and Midjourney work?
First, DALL-E. DALL-E is a generative AI model based on the transformer architecture with an *autoregressive transformer*.

An *autoregressive transformer* defines how a model generates images from text descriptions, it generates one pixel at a time, and then uses the generated pixels to generate the next pixel. Passing through multiple layers in a neural network, until the image is complete.

With this process, DALL-E, controls attributes, objects, characteristics, and more in the image it generates. However, DALL-E 2 and 3 have more control over the generated images.


## Additional Capabilities of Image Generation
You've seen so far how we were able to generate an image using a few lines in Python. However, there are more things you can do with images.

You can also do the following:
- **Perform edits**. By providing an existing image a mask and a prompt, you can alter an image. For example, you can add something to a portion of an image. Imagine our bunny image, you can add a hat to the bunny. How you would do that is by providing the image, a mask and a text prompt to say what should be done. (Note: this is not supported in DALL-E 3.)

Here is an example using GPT Image:
```python
response = client.images.edit(
    model="gpt-image-1",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo."
)
image_url = response.data[0].url
```

- **Create variations**. The idea is that you take an existing image and ask that variations are created. To create a variation, you provide an image and a text prompt and code like so:

```python
response = openapi.Image.create_variation(
    image=open("bunny.png", "rb"),
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
```


## Temperature
Temperature is a parameter that controls the randomness of the output of a Generative AI model. The temperature is a value between 0 and 1, where 0 means that the output is deterministic and 1 means that the output is random. The default value is 0.7.

Let's look at an example of how the temperature works, by running this prompt twice:
> Prompt: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils."

![image_1](/09-building-image-applications/images/Screenshot%202026-05-21%20at%207.08.55 AM.png)

Now let's run the same prompt just to see that we won't get the same image twice:

![image_2](/09-building-image-applications/images/Screenshot%202026-05-21%20at%207.09.17 AM.png)

### Changing the Temperature
So let's try to make the response more deterministic. We could observe from the two images we generated that in the first image, there's a bunny and in the second image, there's a horse, so the images vary greatly.

Let's therefore change our code and set the temperature to 0.
```python
generation_response = client.images.create(
    prompt="Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils.",
    size="1024x1024",
    n=2,
    temperature=0
)
```

Now when you run this code, you get two images.

![image_3](/09-building-image-applications/images/Screenshot%202026-05-21%20at%207.32.40 AM.png)

![image_4](/09-building-image-applications/images/Screenshot%202026-05-21%20at%207.32.57 AM.png)

Here you can clearly see how the images resemble each other more.