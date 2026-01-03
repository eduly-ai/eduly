from manim import *

# Set vertical resolution
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.0
config.frame_width = 8.0

class MultiHeadAttentionScene(Scene):
    def construct(self):
        # --- Caption Bar Setup ---
        self.caption_bg = Rectangle(width=8, height=2.0, fill_color=BLACK, fill_opacity=0.8)
        self.caption_bg.to_edge(DOWN, buff=0)
        self.caption_bg.set_z_index(1000)
        
        self.caption_text = Text("Understanding Multi-Head Attention", font_size=28, color=WHITE)
        self.caption_text.move_to(self.caption_bg.get_center())
        self.caption_text.set_z_index(1001)
        
        self.add(self.caption_bg, self.caption_text)
        
        # --- Scene 0: Opening ---
        header = Text("Part 4/7: Attention Is All You Need", font_size=24, color=GRAY)
        header.to_edge(UP, buff=0.5)
        
        title = Text("Multi-Head Attention", font_size=48, color=BLUE).next_to(header, DOWN, buff=0.5)
        subtitle = Text("Seeing in Parallel", font_size=36, color=WHITE).next_to(title, DOWN, buff=0.2)
        
        self.play(FadeIn(header), Write(title), FadeIn(subtitle))
        self.wait(2)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Move to Scene 1
        self.scene_1_weighted_average()
        self.scene_2_multi_head_split()
        self.scene_3_parallel_perspectives()
        self.scene_4_math_scaling()
        self.scene_5_concatenation()
        self.scene_6_final_projection()
        self.scene_7_gqa_mqa()
        self.scene_8_closing()

    def update_caption(self, text_str):
        new_text = Text(text_str, font_size=28, color=WHITE)
        # Basic line wrapping
        if len(text_str) > 40:
             new_text = Text(text_str, font_size=24, color=WHITE)
             
        # Manually wrap if width > 7.5
        if new_text.width > 7.5:
            # Simple word wrap strategy or just scale down
            new_text.scale(7.5 / new_text.width)
            
        new_text.move_to(self.caption_bg.get_center())
        new_text.set_z_index(1001)
        
        self.play(Transform(self.caption_text, new_text), run_time=0.5)
        self.wait(0.5)

    def scene_1_weighted_average(self):
        self.update_caption("The Problem of the Weighted Average")
        
        # Sentence construction
        sentence_str = "The chef cooked the meal that was delicious"
        words_text = sentence_str.split()
        self.words = VGroup(*[Text(w, font_size=32) for w in words_text])
        self.words.arrange(RIGHT, buff=0.15).shift(UP * 2)
        
        # Ensure it fits width
        if self.words.width > 7.5:
            self.words.scale(7.5 / self.words.width)
            
        w_chef = self.words[1]
        w_meal = self.words[4]
        self.w_that = self.words[5]
        
        self.play(Write(self.words))
        self.wait(0.5)
        
        # Highlight 'that'
        self.that_rect = SurroundingRectangle(self.w_that, color=GOLD, buff=0.1)
        self.play(Create(self.that_rect))
        
        # Arrows
        arrow_chef = Arrow(start=self.w_that.get_bottom(), end=w_chef.get_bottom(), color=RED, buff=0.1, path_arc=0.5)
        arrow_meal = Arrow(start=self.w_that.get_bottom(), end=w_meal.get_bottom(), color=BLUE, buff=0.1, path_arc=-0.5)
        
        self.play(GrowArrow(arrow_chef), GrowArrow(arrow_meal))
        
        # Bar chart above
        chart_axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 1, 0.5],
            x_length=3,
            y_length=2,
            axis_config={"include_tip": False, "include_numbers": False}
        ).next_to(self.words, UP, buff=1.5)
        
        bar_chef = Rectangle(width=0.8, height=1.5, color=RED, fill_opacity=0.8)
        bar_meal = Rectangle(width=0.8, height=1.5, color=BLUE, fill_opacity=0.8)
        
        # Position bars manually on axes or just relative
        bar_chef.move_to(chart_axes.c2p(0.8, 0.5)) # rough pos
        bar_chef.align_to(chart_axes.x_axis, DOWN)
        bar_meal.move_to(chart_axes.c2p(2.2, 0.5))
        bar_meal.align_to(chart_axes.x_axis, DOWN)
        
        label_chef = Text("Chef", font_size=20).next_to(bar_chef, DOWN)
        label_meal = Text("Meal", font_size=20).next_to(bar_meal, DOWN)
        
        self.play(FadeIn(chart_axes), GrowFromEdge(bar_chef, DOWN), GrowFromEdge(bar_meal, DOWN), FadeIn(label_chef), FadeIn(label_meal))
        
        # Blurring/Muddying
        muddy_color = "#8B8000"
        self.play(
            self.w_that.animate.set_color(muddy_color),
            self.that_rect.animate.set_color(muddy_color),
            FadeOut(arrow_chef),
            FadeOut(arrow_meal),
            FadeOut(chart_axes),
            FadeOut(bar_chef),
            FadeOut(bar_meal),
            FadeOut(label_chef),
            FadeOut(label_meal)
        )
        self.wait(1)


    def scene_2_multi_head_split(self):
        self.update_caption("Splitting into Multi-Head Attention")
        
        # Clean up
        self.play(FadeOut(self.words), FadeOut(self.that_rect))
        
        # Input Vector
        input_vector = VGroup(*[Square(side_length=0.4, fill_color=WHITE, fill_opacity=1) for _ in range(8)])
        input_vector.arrange(DOWN, buff=0)
        input_vector.move_to(UP * 4)
        label_vec = Text("'that' (512d)", font_size=24).next_to(input_vector, LEFT)
        
        self.play(FadeIn(input_vector), FadeIn(label_vec))
        
        # Prism
        prism = Triangle(color=WHITE, fill_opacity=0.5, fill_color=BLUE_D).scale(1.5)
        prism.move_to(UP * 1)
        label_prism = Text("Linear Projections", font_size=24).next_to(prism, RIGHT)
        
        self.play(FadeIn(prism), FadeIn(label_prism))
        self.play(input_vector.animate.next_to(prism, UP, buff=0.5), label_vec.animate.next_to(prism, UP, buff=0.5).shift(LEFT*2))
        
        # Output Heads
        heads = VGroup()
        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]
        
        for i in range(8):
            vec = VGroup(*[Square(side_length=0.2, fill_color=colors[i], fill_opacity=1, stroke_width=1) for _ in range(4)])
            vec.arrange(DOWN, buff=0)
            lbl = Text(f"H{i+1}", font_size=20, color=colors[i]).next_to(vec, UP, buff=0.1)
            grp = VGroup(lbl, vec)
            heads.add(grp)
            
        heads.arrange_in_grid(rows=2, cols=4, buff=1.0)
        heads.move_to(DOWN * 3)
        
        # Animate split through prism
        self.play(
            LaggedStart(
                *[TransformFromCopy(input_vector, head) for head in heads],
                lag_ratio=0.1
            ),
            run_time=2
        )
        
        dim_lbl = Text("Dimension = 64 per Head", font_size=24).next_to(heads, DOWN, buff=0.5)
        self.play(Write(dim_lbl))
        self.wait(1)
        
        self.scene_2_objects = VGroup(input_vector, label_vec, prism, label_prism, heads, dim_lbl)


    def scene_3_parallel_perspectives(self):
        self.update_caption("Parallel Perspectives: Different Roles")
        
        self.play(FadeOut(self.scene_2_objects))
        
        # Helper to create a sentence block
        def create_block(title_text, title_color):
            g = VGroup()
            title = Text(title_text, color=title_color, font_size=28)
            
            line1_words = ["The", "chef", "cooked", "the", "meal"]
            line2_words = ["that", "was", "delicious"]
            
            l1 = VGroup(*[Text(w, font_size=24) for w in line1_words]).arrange(RIGHT, buff=0.15)
            l2 = VGroup(*[Text(w, font_size=24) for w in line2_words]).arrange(RIGHT, buff=0.15)
            
            words = VGroup(l1, l2).arrange(DOWN, buff=0.2)
            
            title.next_to(words, UP, buff=0.4)
            g.add(title, words)
            return g, l1, l2

        # Panel 1
        panel1, p1_l1, p1_l2 = create_block("Head 1: Object Reference", BLUE)
        panel1.move_to(UP * 2.5)
        
        # Arrow: that (l2[0]) -> meal (l1[4])
        arrow1 = Arrow(start=p1_l2[0].get_top(), end=p1_l1[4].get_bottom(), color=BLUE, buff=0.05)
        
        # Panel 2
        panel2, p2_l1, p2_l2 = create_block("Head 2: Subject-Verb", RED)
        panel2.move_to(DOWN * 2.5)
        
        # Arrow: cooked (l1[2]) -> chef (l1[1])
        arrow2 = Arrow(start=p2_l1[2].get_bottom(), end=p2_l1[1].get_bottom(), color=RED, buff=0.05, path_arc=0.5)
        
        self.play(FadeIn(panel1))
        self.play(GrowArrow(arrow1))
        self.wait(1)
        
        self.play(FadeIn(panel2))
        self.play(GrowArrow(arrow2))
        self.wait(2)
        
        self.scene_3_objects = VGroup(panel1, arrow1, panel2, arrow2)


    def scene_4_math_scaling(self):
        self.update_caption("Scaling Down: Efficient Computation")
        self.play(FadeOut(self.scene_3_objects))
        
        # Large Rectangle representing 512 dimensions
        big_rect = Rectangle(width=6, height=3, color=WHITE, fill_opacity=0.1)
        big_label = Text("Model Dimension: 512", font_size=32).next_to(big_rect, UP)
        
        self.play(Create(big_rect), Write(big_label))
        self.wait(0.5)
        
        # Visualizing the split
        split_rects = VGroup(*[Rectangle(width=6/8 - 0.05, height=3, color=BLUE_C, fill_opacity=0.3) for _ in range(8)])
        split_rects.arrange(RIGHT, buff=0.05)
        split_rects.move_to(big_rect)
        
        self.play(ReplacementTransform(big_rect, split_rects))
        
        # Isolate one head
        keep_idx = 3
        head_rect = split_rects[keep_idx]
        others = VGroup(*[split_rects[i] for i in range(8) if i != keep_idx])
        
        self.play(
            FadeOut(others),
            FadeOut(big_label),
            head_rect.animate.scale(2).move_to(UP * 1)
        )
        
        # Labels
        head_label = Text("Head Dimension: 64", font_size=32).next_to(head_rect, UP, buff=0.5)
        self.play(Write(head_label))
        
        # Internal components (Q, K, V)
        qkv_group = VGroup(
            Text("Query", font_size=20, color=BLUE),
            Text("Key", font_size=20, color=GOLD),
            Text("Value", font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.3).move_to(head_rect)
        
        self.play(Write(qkv_group))
        
        # Math Equation
        equation = MathTex(r"d_{head} = \frac{d_{model}}{h} = \frac{512}{8} = 64", font_size=36)
        equation.next_to(head_rect, DOWN, buff=1.0)
        
        self.play(Write(equation))
        self.wait(2)
        
        self.scene_4_objects = VGroup(head_rect, head_label, qkv_group, equation)


    def scene_5_concatenation(self):
        self.update_caption("Recombining: Concatenation")
        self.play(FadeOut(self.scene_4_objects))
        
        # Create scattered vectors
        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]
        vectors = VGroup()
        for i in range(8):
            v = VGroup(*[Square(side_length=0.25, fill_color=colors[i], fill_opacity=1, stroke_width=1) for _ in range(4)])
            v.arrange(DOWN, buff=0)
            vectors.add(v)
            
        vectors.arrange_in_grid(rows=2, cols=4, buff=1.0)
        self.play(FadeIn(vectors))
        self.wait(0.5)
        
        # Stack animation
        stack_target = vectors.copy()
        stack_target.arrange(DOWN, buff=0)
        stack_target.move_to(ORIGIN)
        
        self.play(Transform(vectors, stack_target), run_time=1.5)
        
        label = Text("Concatenated Output", font_size=24).next_to(vectors, RIGHT, buff=0.5)
        label_dim = Text("512 Dimensions", font_size=20, color=GRAY).next_to(label, DOWN)
        brace = Brace(vectors, LEFT)
        
        self.play(Create(brace), Write(label), Write(label_dim))
        self.wait(1)
        
        self.scene_5_objects = VGroup(vectors, label, label_dim, brace)


    def scene_6_final_projection(self):
        self.update_caption("Final Projection: Mixing Information")
        
        # Cleanup
        stack = self.scene_5_objects[0]
        self.play(FadeOut(self.scene_5_objects[1:]))
        
        # Setup Matrix W_O
        w_o = Rectangle(width=2, height=9, color=WHITE, fill_opacity=0.3, fill_color=GRAY)
        w_o_label = MathTex("W_O", font_size=48).move_to(w_o)
        
        # Move stack left
        self.play(stack.animate.move_to(LEFT * 2.5))
        
        w_o.move_to(ORIGIN)
        w_o_label.move_to(ORIGIN)
        
        self.play(FadeIn(w_o), FadeIn(w_o_label))
        
        # Output Vector
        output_vec = VGroup(*[Square(side_length=0.25, fill_color=GOLD, fill_opacity=1, stroke_width=1) for _ in range(32)])
        output_vec.arrange(DOWN, buff=0)
        output_vec.move_to(ORIGIN) # Starts at matrix
        
        # Animation
        self.play(stack.animate.move_to(ORIGIN), run_time=1)
        self.play(
            FadeOut(stack),
            FadeIn(output_vec),
            output_vec.animate.move_to(RIGHT * 2.5),
            run_time=1
        )
        
        # Glow effect
        glow = output_vec.copy().set_color(YELLOW).set_opacity(0.5).scale(1.1)
        self.play(FadeIn(glow, run_time=0.5))
        self.play(FadeOut(glow, run_time=0.5))
        
        label = Text("Integrated Context", font_size=24).next_to(output_vec, UP)
        self.play(Write(label))
        self.wait(1)
        
        self.scene_6_objects = VGroup(output_vec, w_o, w_o_label, label)


    def scene_7_gqa_mqa(self):
        self.update_caption("Modern Variations: GQA & MQA")
        self.play(FadeOut(self.scene_6_objects))
        
        # MHA Visualization (Top)
        mha_title = Text("Standard Multi-Head Attention", font_size=24).move_to(UP * 6)
        
        def create_col(count, color, name):
            g = VGroup(*[Square(side_length=0.3, fill_color=color, fill_opacity=1, stroke_width=1) for _ in range(count)])
            g.arrange(DOWN, buff=0.05)
            lbl = Text(name, font_size=16).next_to(g, UP, buff=0.1)
            return VGroup(g, lbl)
            
        q_mha = create_col(8, BLUE, "Q")
        k_mha = create_col(8, GOLD, "K")
        v_mha = create_col(8, GREEN, "V")
        
        mha_viz = VGroup(q_mha, k_mha, v_mha).arrange(RIGHT, buff=0.5).next_to(mha_title, DOWN, buff=0.5)
        
        self.play(Write(mha_title), FadeIn(mha_viz))
        
        # GQA Visualization (Bottom)
        gqa_title = Text("Grouped-Query Attention (GQA)", font_size=24).move_to(DOWN * 0.5)
        
        q_gqa_blocks = VGroup(*[Square(side_length=0.3, fill_color=BLUE, fill_opacity=1, stroke_width=1) for _ in range(8)])
        q_gqa_blocks.arrange(DOWN, buff=0.05)
        q_gqa_lbl = Text("Q", font_size=16).next_to(q_gqa_blocks, UP, buff=0.1)
        q_gqa = VGroup(q_gqa_blocks, q_gqa_lbl)
        
        # K and V (Only 2 blocks each)
        # Position them to align with Q groups
        k_gqa_blocks = VGroup(
            Square(side_length=0.3, fill_color=GOLD, fill_opacity=1, stroke_width=1),
            Square(side_length=0.3, fill_color=GOLD, fill_opacity=1, stroke_width=1)
        )
        # Manually position
        # Q has height approx 2.8. Top y, Bottom y.
        # K1 aligns with Q[1.5] (between 1 and 2), K2 with Q[5.5]
        k_gqa_blocks[0].move_to(q_gqa_blocks[1].get_bottom() + DOWN*0.025 + RIGHT*1.5) # approximate
        k_gqa_blocks[1].move_to(q_gqa_blocks[5].get_bottom() + DOWN*0.025 + RIGHT*1.5)
        
        k_gqa_lbl = Text("K", font_size=16).next_to(k_gqa_blocks[0], UP, buff=0.1).shift(UP * 0.7) # Align with Q label roughly
        k_gqa = VGroup(k_gqa_blocks, k_gqa_lbl)

        v_gqa_blocks = k_gqa_blocks.copy().set_color(GREEN)
        v_gqa_blocks.next_to(k_gqa_blocks, RIGHT, buff=0.5)
        v_gqa_lbl = Text("V", font_size=16).next_to(v_gqa_blocks[0], UP, buff=0.1).shift(UP * 0.7)
        v_gqa = VGroup(v_gqa_blocks, v_gqa_lbl)
        
        gqa_viz = VGroup(q_gqa, k_gqa, v_gqa) # Positions already set relative
        gqa_viz.move_to(DOWN * 3.5)
        
        self.play(Write(gqa_title), FadeIn(gqa_viz))
        
        # Draw lines for GQA
        lines = VGroup()
        for i in range(4):
            l = Line(q_gqa_blocks[i].get_right(), k_gqa_blocks[0].get_left(), color=GRAY, stroke_width=1, stroke_opacity=0.5)
            lines.add(l)
        for i in range(4, 8):
            l = Line(q_gqa_blocks[i].get_right(), k_gqa_blocks[1].get_left(), color=GRAY, stroke_width=1, stroke_opacity=0.5)
            lines.add(l)
            
        self.play(Create(lines))
        
        saving_text = Text("Reduces Memory & Faster Inference", font_size=20, color=GREEN).next_to(gqa_viz, DOWN)
        self.play(Write(saving_text))
        self.wait(2)
        
        self.scene_7_objects = VGroup(mha_title, mha_viz, gqa_title, gqa_viz, lines, saving_text)


    def scene_8_closing(self):
        self.update_caption("Clarity through Diversity")
        self.play(FadeOut(self.scene_7_objects))
        
        # Word Grid
        word_list = ["Context", "Syntax", "Meaning", "Logic", "Time", "Space", "Value", "Query", 
                     "Key", "Head", "Layer", "Norm", "Deep", "Learn", "Scale", "Mask",
                     "Vector", "Matrix", "Tensor", "Bias", "Weight", "Data", "Model", "Code"]
        
        grid = VGroup(*[Text(w, font_size=18, color=GRAY_C) for w in word_list])
        grid.arrange_in_grid(rows=6, cols=4, buff=1.0)
        
        self.play(FadeIn(grid, lag_ratio=0.05))
        
        # Flashing connections
        lines = VGroup()
        colors = [RED, BLUE, GREEN, GOLD, PURPLE, TEAL]
        import random
        # Seed for reproducibility if needed, but random is fine here
        
        for _ in range(15):
            idx1 = random.randint(0, len(grid)-1)
            idx2 = random.randint(0, len(grid)-1)
            if idx1 != idx2:
                l = Line(grid[idx1].get_center(), grid[idx2].get_center(), color=random.choice(colors), stroke_width=2, stroke_opacity=0.8)
                lines.add(l)
                
        self.play(Create(lines, lag_ratio=0.1), run_time=2)
        
        # Title Overlay
        title_box = Rectangle(width=7, height=2, fill_color=BLACK, fill_opacity=0.85, stroke_width=0)
        final_title = Text("Multi-Head Attention", font_size=42, color=WHITE).move_to(title_box.get_center()).shift(UP*0.3)
        subtitle = Text("Seeing in Parallel", font_size=32, color=BLUE).next_to(final_title, DOWN, buff=0.2)
        
        overlay = VGroup(title_box, final_title, subtitle).move_to(ORIGIN)
        
        self.play(FadeIn(overlay))
        self.wait(2)
        
        # Transition to Takeaways
        self.play(
            FadeOut(grid), FadeOut(lines), FadeOut(overlay),
            FadeOut(self.caption_bg), FadeOut(self.caption_text)
        )
        
        # Summary
        summary_title = Text("Key Takeaways", font_size=40, color=BLUE).to_edge(UP, buff=1.5)
        
        points = [
            "Parallel heads capture diverse relationships",
            "Projects 512d to 8 x 64d subspaces",
            "Outputs are concatenated back to 512d",
            "GQA shares Key/Value heads for speed"
        ]
        
        bullets = VGroup()
        for p in points:
            t = Text("• " + p, font_size=26, color=WHITE)
            if t.width > 7.5:
                t.scale(7.5 / t.width)
            bullets.add(t)
            
        bullets.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        bullets.next_to(summary_title, DOWN, buff=0.5)
        
        self.play(Write(summary_title), FadeIn(bullets, lag_ratio=0.3))
        self.wait(2)
        
        # Next Topic Teaser
        next_topic = Text("Next: Positional Encoding", font_size=36, color=GOLD).next_to(bullets, DOWN, buff=1.5)
        teaser = Text("Giving Order to Chaos", font_size=28, color=GRAY_A).next_to(next_topic, DOWN, buff=0.2)
        
        self.play(FadeIn(next_topic), FadeIn(teaser))
        self.wait(3)
        
        self.play(FadeOut(summary_title), FadeOut(bullets), FadeOut(next_topic), FadeOut(teaser))

