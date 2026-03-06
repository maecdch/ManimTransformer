from manim import *
import math
import random

# --- Visual Style Configuration ---
# Cyberpunk Color Palette
NEON_BLUE = "#00f2ff"
FLUORESCENT_GREEN = "#39ff14"
CYBER_PURPLE = "#bc13fe"
DARK_BG = "#0a0a0a"
GRID_COLOR = "#1f1f1f"

# Text Styles
TITLE_FONT_SIZE = 32
SUBTITLE_FONT_SIZE = 20
FORMULA_FONT_SIZE = 36

class CyberGrid(VGroup):
    """Custom Cyberpunk Background Grid"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": NEON_BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.15
            },
            axis_config={"stroke_opacity": 0} # Hide axes
        )
        self.add(plane)
        
        # Add random glowing dots on intersections
        for _ in range(20):
            dot = Dot(
                point=plane.c2p(random.randint(-7, 7), random.randint(-4, 4)),
                color=NEON_BLUE,
                radius=0.05,
                fill_opacity=0.6
            )
            self.add(dot)

class TransformerFlow(Scene):
    def construct(self):
        # 1. Setup Environment
        self.camera.background_color = DARK_BG
        self.setup_background()
        
        # 2. Load Data
        script_data = self.get_script_data()
        
        # 3. Iterate Steps
        for step in script_data:
            self.play_step(step)
            self.wait(2)
            self.clear_scene()

    def setup_background(self):
        # Static Grid
        grid = CyberGrid()
        self.add(grid)
        
        # Dynamic Lighting (Moving Glow)
        light_source = Dot(radius=0).move_to(LEFT * 5)
        glow = Dot(radius=3, color=CYBER_PURPLE).set_opacity(0.1)
        glow.add_updater(lambda m: m.move_to(light_source.get_center()))
        
        def update_light(m, dt):
            t = self.time * 0.5
            m.move_to(np.array([
                4 * math.sin(t),
                3 * math.cos(t * 1.3),
                0
            ]))
            
        light_source.add_updater(update_light)
        self.add(light_source, glow)
        self.background_elements = VGroup(grid, light_source, glow)

    def get_script_data(self):
        return [
            {
                "step_number": 1,
                "title_zh": "序列的瓶颈：RNN的局限",
                "title_en": "The Sequence Bottleneck: RNN's Limitations",
                "formula": r"h_t = f(h_{t-1}, x_t)",
                "type": "rnn"
            },
            {
                "step_number": 2,
                "title_zh": "自注意力机制：全局洞察力",
                "title_en": "Self-Attention: Global Insight",
                "formula": r"\text{Attention}(Q, K, V)",
                "type": "self_attention"
            },
            {
                "step_number": 3,
                "title_zh": "QKV投影：构建核心",
                "title_en": "QKV Projection: Building the Core",
                "formula": r"Q = X W_Q, K = X W_K, V = X W_V",
                "type": "qkv"
            },
            {
                "step_number": 4,
                "title_zh": "点积缩放注意力：权重与聚合",
                "title_en": "Scaled Dot-Product Attention",
                "formula": r"\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V",
                "type": "scaled_attention"
            },
            {
                "step_number": 5,
                "title_zh": "多头注意力：捕捉多维度信息",
                "title_en": "Multi-Head Attention",
                "formula": r"\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O",
                "type": "multi_head"
            },
            {
                "step_number": 6,
                "title_zh": "位置编码：注入序列秩序",
                "title_en": "Positional Encoding",
                "formula": r"PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})",
                "type": "positional_encoding"
            },
            {
                "step_number": 7,
                "title_zh": "Transformer块：构建深层网络",
                "title_en": "Transformer Block",
                "formula": r"\text{LayerNorm}(x + \text{Sublayer}(x))",
                "type": "transformer_block"
            },
            {
                "step_number": 8,
                "title_zh": "能力边界：输出与未来展望",
                "title_en": "Capability Frontier",
                "formula": r"\text{AI} \rightarrow \infty",
                "type": "future"
            }
        ]

    def play_step(self, step):
        # --- Title Section ---
        title_zh = Text(step["title_zh"], font_size=TITLE_FONT_SIZE, color=NEON_BLUE)
        title_en = Text(step["title_en"], font_size=SUBTITLE_FONT_SIZE, color=WHITE).set_opacity(0.8)
        
        title_group = VGroup(title_zh, title_en).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        
        bg_rect = BackgroundRectangle(title_group, color=BLACK, fill_opacity=0.7, buff=0.2)
        
        self.play(FadeIn(bg_rect), Write(title_group), run_time=1)
        self.current_title = VGroup(bg_rect, title_group)

        # --- Formula Section ---
        if step["formula"]:
            # Use MathTex for LaTeX formulas
            formula = MathTex(step["formula"], color=FLUORESCENT_GREEN, font_size=FORMULA_FONT_SIZE)
            formula.to_edge(DOWN, buff=1)
            # Cyber scan effect
            scan_line = Line(formula.get_left(), formula.get_left(), color=NEON_BLUE)
            scan_line.set_height(formula.get_height() + 0.2)
            
            self.add(formula)
            self.play(
                ShowPassingFlash(
                    scan_line.copy().set_points_as_corners([formula.get_left(), formula.get_right()]),
                    time_width=0.5,
                    run_time=1.5
                ),
                AddTextLetterByLetter(formula, run_time=1.5)
            )
            self.current_formula = formula
        else:
            self.current_formula = VGroup()

        # --- Visual Animation Section ---
        visual_method = getattr(self, f"animate_{step['type']}", None)
        if visual_method:
            self.current_visuals = visual_method()
        else:
            self.current_visuals = VGroup()

    def clear_scene(self):
        # Fade out everything except background
        anims = [FadeOut(self.current_title), FadeOut(self.current_formula), FadeOut(self.current_visuals)]
        self.play(*anims)

    # -------------------------------------------------------------------------
    # Specific Animations
    # -------------------------------------------------------------------------

    def animate_rnn(self):
        # Visual: Sequence of nodes, arrows fading
        nodes = VGroup(*[
            Square(side_length=0.8, color=NEON_BLUE, fill_opacity=0.5)
            for _ in range(5)
        ]).arrange(RIGHT, buff=1)
        
        arrows = VGroup()
        for i in range(4):
            arrow = Arrow(nodes[i].get_right(), nodes[i+1].get_left(), color=WHITE, buff=0.1)
            arrows.add(arrow)
            
        group = VGroup(nodes, arrows).move_to(ORIGIN)
        
        self.play(LaggedStart(*[Create(n) for n in nodes], lag_ratio=0.2))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))
        
        # Highlight long distance problem
        long_arrow = CurvedArrow(nodes[0].get_top(), nodes[4].get_top(), angle=-PI/4, color=RED)
        cross = Cross(long_arrow, stroke_color=RED)
        
        self.play(Create(long_arrow))
        self.play(Create(cross))
        
        return VGroup(group, long_arrow, cross)

    def animate_self_attention(self):
        # Visual: Central word, connecting lines
        words = VGroup(*[
            Text(w, font_size=24, color=WHITE) 
            for w in ["The", "animal", "didn't", "cross", "street"]
        ]).arrange(RIGHT, buff=1)
        
        self.play(Write(words))
        
        center_idx = 1 # "animal"
        center_word = words[center_idx]
        center_word.set_color(NEON_BLUE)
        
        lines = VGroup()
        for i, word in enumerate(words):
            if i == center_idx: continue
            
            # Thickness based on "attention"
            stroke = 4 if i == 4 else 1 # High attention to "street"
            col = FLUORESCENT_GREEN if i == 4 else GREY
            
            line = Line(word.get_bottom(), center_word.get_bottom() + DOWN*2)
            # Use cubic bezier for nice curves
            curve = CubicBezier(
                word.get_bottom(),
                word.get_bottom() + DOWN,
                center_word.get_bottom() + DOWN,
                center_word.get_bottom(),
                color=col,
                stroke_width=stroke
            )
            lines.add(curve)
            
        self.play(Create(lines, run_time=2))
        return VGroup(words, lines)

    def animate_qkv(self):
        # Visual: X (Blue) -> W (Green) -> QKV (Purple)
        input_x = Rectangle(height=2, width=1, color=NEON_BLUE, fill_opacity=0.3).move_to(LEFT * 4)
        input_label = Text("X", color=NEON_BLUE).move_to(input_x)
        
        weights = VGroup(*[
            Rectangle(height=1.5, width=1, color=FLUORESCENT_GREEN, fill_opacity=0.3)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        weight_labels = VGroup(*[
            MathTex(t, font_size=24, color=FLUORESCENT_GREEN).move_to(w)
            for w, t in zip(weights, ["W_Q", "W_K", "W_V"])
        ])
        
        outputs = VGroup(*[
            Rectangle(height=1.5, width=1, color=CYBER_PURPLE, fill_opacity=0.3)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.5).move_to(RIGHT * 4)
        output_labels = VGroup(*[
            MathTex(t, font_size=24, color=CYBER_PURPLE).move_to(o)
            for o, t in zip(outputs, ["Q", "K", "V"])
        ])
        
        arrows1 = VGroup(*[
            Arrow(input_x.get_right(), w.get_left(), color=WHITE, buff=0.2)
            for w in weights
        ])
        
        arrows2 = VGroup(*[
            Arrow(w.get_right(), o.get_left(), color=WHITE, buff=0.2)
            for w, o in zip(weights, outputs)
        ])
        
        self.play(Create(input_x), Write(input_label))
        self.play(LaggedStart(
            *[AnimationGroup(Create(a), Create(w), Write(l)) 
              for a, w, l in zip(arrows1, weights, weight_labels)],
            lag_ratio=0.3
        ))
        self.play(LaggedStart(
            *[AnimationGroup(Create(a), Create(o), Write(l)) 
              for a, o, l in zip(arrows2, outputs, output_labels)],
            lag_ratio=0.3
        ))
        
        return VGroup(input_x, input_label, weights, weight_labels, outputs, output_labels, arrows1, arrows2)

    def animate_scaled_attention(self):
        # Visual: Q * K^T -> Scale -> Softmax -> * V
        q = Square(side_length=1, color=CYBER_PURPLE, fill_opacity=0.5).move_to(LEFT * 5)
        k = Square(side_length=1, color=CYBER_PURPLE, fill_opacity=0.5).move_to(LEFT * 3)
        
        # Operation symbols
        times = MathTex(r"\times", font_size=50).move_to(LEFT * 4)
        
        # Result of QK
        score = Rectangle(width=1.5, height=1, color=WHITE).move_to(LEFT * 1)
        
        # Softmax block
        softmax = RoundedRectangle(corner_radius=0.2, width=2, height=1, color=FLUORESCENT_GREEN).move_to(RIGHT * 2)
        softmax_txt = Text("Softmax", font_size=20).move_to(softmax)
        
        # V
        v = Square(side_length=1, color=CYBER_PURPLE, fill_opacity=0.5).move_to(RIGHT * 4)
        
        # Final
        final = Rectangle(width=1, height=1, color=NEON_BLUE, fill_opacity=0.8).move_to(RIGHT * 6)
        
        arrows = VGroup(
            Arrow(k.get_right(), score.get_left()),
            Arrow(score.get_right(), softmax.get_left()),
            Arrow(softmax.get_right(), final.get_left())
        )
        
        self.play(Create(q), Create(k), Write(times))
        self.play(Transform(VGroup(q, k, times), score))
        self.play(Create(arrows[1]), Create(softmax), Write(softmax_txt))
        self.play(Create(v))
        self.play(Create(arrows[2]), Transform(VGroup(softmax, softmax_txt, v), final))
        
        return VGroup(score, final, arrows)

    def animate_multi_head(self):
        # Visual: 1 big block splitting into 4, then merging
        big_block = Rectangle(width=4, height=1, color=NEON_BLUE, fill_opacity=0.5)
        
        heads = VGroup(*[
            Rectangle(width=0.8, height=0.8, color=CYBER_PURPLE, fill_opacity=0.6)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.2)
        
        self.play(Create(big_block))
        self.play(ReplacementTransform(big_block, heads))
        
        # Process (wiggle)
        self.play(heads.animate.shift(UP * 0.5), run_time=0.5)
        self.play(heads.animate.shift(DOWN * 0.5), run_time=0.5)
        
        # Merge back
        final_block = Rectangle(width=4, height=1, color=FLUORESCENT_GREEN, fill_opacity=0.5)
        self.play(ReplacementTransform(heads, final_block))
        
        return final_block

    def animate_positional_encoding(self):
        # Visual: Bar chart + Sine wave
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            x_length=6,
            y_length=3,
            axis_config={"color": GREY}
        )
        
        # Input embedding (bars)
        bars = VGroup(*[
            Rectangle(width=0.4, height=random.uniform(0.5, 2), color=NEON_BLUE, fill_opacity=0.5)
            .move_to(axes.c2p(i, 0), aligned_edge=DOWN)
            for i in range(1, 9)
        ])
        
        # PE (Wave)
        sine_curve = axes.plot(lambda x: 0.8 * math.sin(x), color=FLUORESCENT_GREEN)
        
        self.play(Create(axes), Create(bars))
        self.play(Create(sine_curve))
        
        # Combine
        combined_bars = VGroup()
        for i, bar in enumerate(bars):
            val = bar.height + 0.8 * math.sin(i+1)
            new_bar = Rectangle(width=0.4, height=abs(val), color=CYBER_PURPLE, fill_opacity=0.8)
            new_bar.move_to(axes.c2p(i+1, 0), aligned_edge=DOWN)
            combined_bars.add(new_bar)
            
        self.play(Transform(bars, combined_bars), FadeOut(sine_curve))
        
        return VGroup(axes, bars)

    def animate_transformer_block(self):
        # Visual: Stacked blocks
        # [ Add & Norm ]
        # [ Feed Fwd   ]
        # [ Add & Norm ]
        # [ Multi-Head ]
        
        blocks = VGroup(
            Rectangle(width=3, height=0.8, color=FLUORESCENT_GREEN, fill_opacity=0.3), # Norm
            Rectangle(width=3, height=1.0, color=NEON_BLUE, fill_opacity=0.3),       # FF
            Rectangle(width=3, height=0.8, color=FLUORESCENT_GREEN, fill_opacity=0.3), # Norm
            Rectangle(width=3, height=1.0, color=CYBER_PURPLE, fill_opacity=0.3)     # Attn
        ).arrange(DOWN, buff=0.2)
        
        labels = ["Add & Norm", "Feed Forward", "Add & Norm", "Multi-Head Attn"]
        texts = VGroup()
        for b, t in zip(blocks, labels):
            texts.add(Text(t, font_size=18).move_to(b))
            
        # Residual connections (curved lines)
        res1 = CurvedArrow(blocks[3].get_left() + LEFT*0.5, blocks[2].get_left() + LEFT*0.5, angle=PI/2, color=WHITE)
        res2 = CurvedArrow(blocks[1].get_left() + LEFT*0.5, blocks[0].get_left() + LEFT*0.5, angle=PI/2, color=WHITE)
        
        group = VGroup(blocks, texts, res1, res2).move_to(ORIGIN)
        
        self.play(LaggedStart(*[Create(b) for b in blocks], lag_ratio=0.2))
        self.play(Write(texts))
        self.play(Create(res1), Create(res2))
        
        return group

    def animate_future(self):
        # Visual: Flashing words
        topics = ["Translation", "Text Generation", "Vision", "Biology", "Robotics"]
        group = VGroup()
        
        for topic in topics:
            t = Text(topic, font_size=60, color=random.choice([NEON_BLUE, FLUORESCENT_GREEN, CYBER_PURPLE]))
            t.move_to(np.array([
                random.uniform(-4, 4),
                random.uniform(-2, 2),
                0
            ]))
            self.play(FadeIn(t, scale=0.5), run_time=0.4)
            self.play(FadeOut(t, scale=1.5), run_time=0.4)
            
        final_text = Text("TRANSFORMER", font_size=80, color=WHITE).set_glow_factor(1)
        self.play(Write(final_text))
        group.add(final_text)
        return group
