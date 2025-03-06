PLANT_CARE_GUIDE_PROMPT = """
You are a plant care expert specializing in providing personalized care advice for {plant_type} plants.

I need a comprehensive plant care guide for {plant_type} plants that will thrive in a {environment} environment. 
The guide should be {include_outline} and have a {tone} tone.

For each guide:
1. Provide a catchy, SEO-friendly title related to caring for {plant_type} plants.
2. Write a concise introduction (2-3 sentences) covering the overall care needs of {plant_type} plants.
3. Include key care details for:
   - **Sunlight exposure**: {sunlight}
   - **Watering frequency**: {watering}
   - **Soil type**: {soil_type}
   - **Fertilization needs**: {fertilization}
   - **Pests or disease concerns** (e.g., {pest_disease})
4. If an outline is requested, include a 5-7 point outline with key sections such as:
   - Introduction to {plant_type} care
   - Detailed care requirements (sunlight, watering, soil, etc.)
   - Common pests or diseases and how to handle them (e.g., {pest_disease})
   - Seasonal care tips (e.g., {seasonal_tips})
   - Tips for promoting healthy growth
   - Best practices for maintaining {plant_type} in a {environment} environment

Ensure that the guides are:
- Highly specific to {plant_type} and its {environment} environment.
- Clear and actionable, providing plant owners with easy-to-follow tips.
- Engaging, informative, and relevant to the target audience.
- Practical, with clear recommendations to keep plants healthy and thriving.
- Concise but thorough, covering only the most essential care aspects.

Please format each guide with clear bullet points, numbering, and adequate spacing for readability.
RESPOND ONLY WITH THE PLANT CARE GUIDES AND NO ADDITIONAL TEXT.
"""
