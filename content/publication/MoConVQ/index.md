---
title: "MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations"
weight: 1
# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Zhenhua Song
- Yuyang Zhou
- Tenglong Ao
- Baoquan Chen
- Libin Liu

# Author notes (optional)
author_notes:
-
-
-
- 
- 
- "Corresponding Authors"

date: "2024-6-01T00:00:00Z"
doi: "10.1145/3658137"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-04T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics(Proceedings of SIGGRAPH2024)*
publication_short: In *SIGGRAPH (Journal Track)*

abstract: "In this work, we present MoConVQ, a novel unified framework for physics-based motion control leveraging scalable discrete representations. Building upon vector quantized variational autoencoders (VQ-VAE) and model-based reinforcement learning, our approach effectively learns motion embeddings from a large, unstructured dataset spanning tens of hours of motion examples. The resultant motion representation not only captures diverse motion skills but also offers a robust and intuitive interface for various applications. We demonstrate the versatility of MoConVQ through several applications: universal tracking control from various motion sources, interactive character control with latent motion representations using supervised learning, physics-based motion generation from natural language descriptions using the GPT framework, and, most interestingly, seamless integration with large language models (LLMs) with in-context learning to tackle complex and abstract tasks.
"

# Summary. An optional shortened abstract.
summary: We present MoConVQ, a uniform framework enabling simulated avatars to acquire diverse skills from large, unstructured datasets. Leveraging a rich and scalable discrete skill representation, MoConVQ supports a broad range of applications, including pose estimation, interactive control, text-to-motion generation, and, more interestingly, integrating motion generation with Large Language Models (LLMs).

tags: [Physics-based Animation]

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
 - name: Paper
   url: https://arxiv.org/abs/2310.10198

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'MoConVQ/'
url_slides: ''
url_source: ''
# url_video:  'https://www.youtube.com/watch?v=ELZ7m4rLCgk'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#- example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---