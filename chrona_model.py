# chrona_ai_model.py

import openai
from three import THREE
import math

class Chrona:
    """
    Chrona AI Model: Advanced AI agent for particle and matter theory exploration
    Developed at Quantum Horizons Laboratory for astrophysical data analysis.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.conversation_history = [
            {
                "role": "system",
                "content": "You are Chrona, an advanced AI research system specializing in particle physics and astrophysics."
            }
        ]
        openai.api_key = self.api_key

    def analyze_input(self, user_input):
        """Processes user input and generates AI response."""
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=250,
                presence_penalty=0.3,
                frequency_penalty=0.3
            )

            ai_response = response['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            return ai_response
        except Exception as e:
            return f"Error: {str(e)}"

# Space Background Visualization
class SpaceVisualizer:
    """Generates an interactive 3D space background using Three.js."""
    def __init__(self):
        self.scene = THREE.Scene()
        self.camera = THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 5000)
        self.camera.position.z = 1000
        self.renderer = THREE.WebGLRenderer()
        self.stars = None

    def create_star_field(self):
        star_geometry = THREE.BufferGeometry()
        star_material = THREE.PointsMaterial({
            'color': 0xFFFFFF,
            'size': 2,
            'transparent': True,
            'opacity': 0.8
        })

        star_vertices = []
        for _ in range(10000):
            x = THREE.MathUtils.randFloatSpread(2000)
            y = THREE.MathUtils.randFloatSpread(2000)
            z = THREE.MathUtils.randFloatSpread(2000)
            star_vertices.extend([x, y, z])

        star_geometry.setAttribute('position', THREE.Float32BufferAttribute(star_vertices, 3))
        self.stars = THREE.Points(star_geometry, star_material)
        self.scene.add(self.stars)

    def render(self):
        self.renderer.setSize(window.innerWidth, window.innerHeight)
        document.body.appendChild(self.renderer.domElement)
        self.animate()

    def animate(self):
        requestAnimationFrame(self.animate)
        self.stars.rotation.x += 0.0005
        self.stars.rotation.y += 0.001
        self.renderer.render(self.scene, self.camera)

# Usage Example
if __name__ == "__main__":
    api_key = "your-api-key-here"
    chrona = Chrona(api_key)

    user_query = "Explain quantum entanglement."
    response = chrona.analyze_input(user_query)
    print("Chrona Response:", response)

    # Space Visualizer
    visualizer = SpaceVisualizer()
    visualizer.create_star_field()
    visualizer.render()
