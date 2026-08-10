from crewai import Task

from agents.trend_agent import trend_agent
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent
from agents.critic_agent import critic_agent
from agents.improvement_agent import improvement_agent


# -----------------------------------
# TREND RESEARCH
# -----------------------------------

trend_task = Task(

    description="""
Research ONE trending opportunity in the {niche} niche.

Return only:

Trend:
Audience:
Season:
Reason:
""",

    expected_output="""
Trend:
Audience:
Season:
Reason:
""",

    agent=trend_agent

)


# -----------------------------------
# PRODUCT CREATION
# -----------------------------------

product_task = Task(

    description="""
Using the trend identified by the Trend Agent,
create EXACTLY ONE marketplace-ready product.

Trend:
{trend}

Niche:
{niche}

Art Style:
{style}

Your response MUST contain every section below.

Return ONLY this format.

Title:
<one title>

Description:
<150-300 words>

Audience:
<ideal customer>

Image Prompt:
<one detailed AI image prompt>

SEO Tags:
tag1, tag2, tag3, tag4, tag5

Keywords:
keyword1, keyword2, keyword3, keyword4, keyword5

Do NOT generate multiple products.
Do NOT generate alternatives.
Do NOT use Markdown.
""",

    expected_output="""
Title:
Description:
Audience:
Image Prompt:
SEO Tags:
Keywords:
""",

    agent=product_agent

)


# -----------------------------------
# SEO
# -----------------------------------

seo_task = Task(

    description="""
You are improving the SEO metadata for an
existing marketplace product.

Product:

{product}

Generate ONLY:

SEO Tags:
tag1, tag2, tag3, tag4, tag5

Keywords:
keyword1, keyword2, keyword3, keyword4, keyword5

Do NOT rewrite the title.
Do NOT rewrite the description.
Do NOT generate an image prompt.
Do NOT provide explanations.

Return ONLY the requested sections.
""",

    expected_output="""
SEO Tags:
Keywords:
""",

    agent=seo_agent

)


# -----------------------------------
# IMAGE PROMPT
# -----------------------------------

prompt_task = Task(

    description="""
You are creating a marketplace image prompt
for an existing product.

Product:

{product}

Generate ONE professional AI image prompt.

The image prompt must:

- Match the product
- Match the niche
- Match the intended audience
- Preserve the product concept
- Be suitable for marketplace artwork
- Avoid copyrighted characters
- Avoid logos and brands

Return ONLY:

Image Prompt:
""",

    expected_output="""
Image Prompt:
""",

    agent=prompt_agent

)


# -----------------------------------
# PRODUCT CRITIC
# -----------------------------------

critic_task = Task(

    description="""
Review ONLY the following marketplace product.

Product:

{product}

Evaluate:

- Title
- Description
- Image Prompt
- SEO Tags
- Keywords

Consider:

- Marketplace quality
- Buyer appeal
- Clarity
- SEO
- Originality
- Product consistency
- Conversion potential

Return ONLY:

Overall Score:
Strengths:
Weaknesses:
Suggestions:
Marketplace Ready:
""",

    expected_output="""
Overall Score:
Strengths:
Weaknesses:
Suggestions:
Marketplace Ready:
""",

    agent=critic_agent

)


# -----------------------------------
# PRODUCT IMPROVEMENT
# -----------------------------------

improvement_task = Task(

    description="""
Improve the existing marketplace product using
the Critic Agent's feedback.

IMPORTANT:

Preserve the original:

- Product concept
- Niche
- Audience
- Overall creative direction

Only make improvements that address the critic's
identified weaknesses.

Do NOT create an unrelated product.

Existing Product:

Title:
{title}

Description:
{description}

Audience:
{audience}

Image Prompt:
{image_prompt}

SEO Tags:
{seo_tags}

Keywords:
{keywords}

Critic Review:
{review}

Return ONLY the improved product using this
exact format:

Title:
<improved title>

Description:
<improved 150-300 word description>

Audience:
<ideal customer>

Image Prompt:
<improved image prompt>

SEO Tags:
tag1, tag2, tag3, tag4, tag5

Keywords:
keyword1, keyword2, keyword3, keyword4, keyword5

Rules:

- Preserve the original product concept.
- Preserve the original niche.
- Preserve the target audience unless the critic identifies
  the audience as incorrect.
- Fix every reasonable weakness identified by the critic.
- Keep successful elements from the original product.
- Do NOT create multiple products.
- Do NOT create alternatives.
- Do NOT include critic commentary.
- Do NOT include strengths.
- Do NOT include weaknesses.
- Do NOT include suggestions.
- Do NOT use Markdown.
""",

    expected_output="""
Title:
Description:
Audience:
Image Prompt:
SEO Tags:
Keywords:
""",

    agent=improvement_agent

)