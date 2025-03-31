
from manim import *

class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1.5, 1.5], y_range=[-0.5,2, 1], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(1)
        t_p = ValueTracker(1)

        def func(x):
            return x**3 + x**4

        def grad(x):
            return 3*x**2 + 4*x**3
        def pemantle_grad(x):
            return 3*x**2 + 4*x**3 + 0.1*(np.random.binomial(1,0.5,1)[0] - 0.5)
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        initial_point_p = [ax.coords_to_point(t_p.get_value(), func(t_p.get_value()))]
        dot = Dot(point=initial_point, color=GOLD_A)
        dot_p = Dot(point=initial_point_p, color=RED)

        values = [1.]
        pemantle = [1.]
        alpha = 0.1
        x = 1.0
        x_p = 1.0
        for i in range(1000):
            x -= alpha*grad(x)
            x_p -= alpha*pemantle_grad(x_p)
            if i % 10 == 0:
                values.append(x)
                pemantle.append(x_p)


        print(pemantle)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        dot_p.add_updater(lambda x: x.move_to(ax.c2p(t_p.get_value(), func(t_p.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot, dot_p)
        for i in range(len(values)):
            self.play(t.animate.set_value(values[i]),t_p.animate.set_value(pemantle[i]),run_time=0.5)

        self.wait()
