---
title: "ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters"
weight: 20
# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Zhenhua Song
- Baoquan Chen
- Libin Liu

# Author notes (optional)
author_notes:
-
-
- 
- "Corresponding Authors"


date: "2022-12-01T00:00:00Z"
doi: "10.1145/3550454.3555434"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-10-13T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics(Proceedings of SIGGRAPH Asia 2022)*
publication_short: In *SIGGRAPH Asia*

abstract: "In this paper, we introduce ControlVAE, a novel model-based framework
for learning generative motion control policies based on variational autoencoders (VAE). Our framework can learn a rich and flexible latent representation of skills and a skill-conditioned generative control policy from a
diverse set of unorganized motion sequences, which enables the generation
of realistic human behaviors by sampling in the latent space and allows
high-level control policies to reuse the learned skills to accomplish a variety
of downstream tasks. In the training of ControlVAE, we employ a learnable
world model to realize direct supervision of the latent space and the control
policy. This world model effectively captures the unknown dynamics of the
simulation system, enabling efficient model-based learning of high-level
downstream tasks. We also learn a state-conditional prior distribution in the
VAE-based generative control policy, which generates a skill embedding that
outperforms the non-conditional priors in downstream tasks. We demonstrate the effectiveness of ControlVAE using a diverse set of tasks, which
allows realistic and interactive control of the simulated characters.
"

# Summary. An optional shortened abstract.
summary: We introduce ControlVAE, a novel model-based framework for learning generative motion control policies, which learns flexible skill embeddings for motion generation and downstream tasks.

tags: [Physics-based Animation]

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
 - name: Video
   url: https://www.youtube.com/watch?v=ELZ7m4rLCgk
 - name: Code
   url: https://github.com/heyuanYao-pku/Control-VAE

url_pdf: 'Control-VAE/static/author_version.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'Control-VAE/'
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