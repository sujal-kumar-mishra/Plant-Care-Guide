# prompt_templates.py

PLANT_CARE_GUIDE_PROMPT = """
You are a plant care expert specializing in providing personalized plant care tips for {plant_type} plants.

I need plant care guides for {plant_type} plants in a {environment} environment. 
The guides should be {include_outline} and have a {tone} tone.

For each guide:
1. Provide a catchy, SEO-friendly title related to the care of {plant_type} plants
2. Write a brief introduction about the plant's care requirements (2-3 sentences)
3. Include key information about:
   - Sunlight exposure: {sunlight}
   - Watering frequency: {watering}
   - Soil type: {soil_type}
   - Fertilization needs: {fertilization}
   - Pests or diseases concerns (e.g., {pest_disease})
4. If outlines are requested, include a 5-7 point outline with key sections, such as:
   - Introduction to the {plant_type} plant care
   - Care requirements (water, sunlight, soil, etc.)
   - Common issues and pests (e.g., {pest_disease})
   - Seasonal tips: {seasonal_tips}
   - Tips for healthy growth
   - Best practices for maintaining {plant_type} in {environment}

Make sure the guides are:
- Specific to the {plant_type} plant and its {environment} environment
- Clear and actionable for plant owners
- Engaging, unique, and tailored to the target audience
- Provide practical advice to help readers maintain healthy plants
- Concise yet informative, covering the essentials for plant care

Format each guide clearly with numbers and proper spacing for readability.
RESPOND ONLY WITH THE PLANT CARE GUIDES AND NO OTHER TEXT.
"""
