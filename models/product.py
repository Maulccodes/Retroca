from dataclasses import dataclass, field


@dataclass
class Product:

    id: str = ""

    product_number: int = 0

    title: str = ""

    description: str = ""

    audience: str = ""

    image_prompt: str = ""

    seo_tags: list = field(default_factory=list)

    keywords: list = field(default_factory=list)

    review: str = ""

    image_path: str = ""

    tags: list = field(default_factory=list)

    created_at: str = ""

    status: str = "draft"

    favorite: bool = False

    downloads: int = 0

    quality: dict = field(default_factory=dict)

    quality_score: int = 0