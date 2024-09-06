import tkinter as tk
from tkinter import messagebox
import webbrowser

def dashboard():
    webbrowser.open("https://andu.jaidrew.co.in/SIH/index.html")

def science_course():
    messagebox.showinfo("Science Course", "Work in progress. Please check back later!")

def open_maths_gui():
    # Create a new top-level window for Maths
    maths_window = tk.Toplevel(root)
    maths_window.title("Maths Course")
    maths_window.geometry("300x200")

    def learn_maps():
        import tkinter as tk
        from tkinter import messagebox
        import pygame
        import math

        # Function for each button's functionality
        def addition():
            import pygame
            import math
            import webbrowser
            # Initialize Pygame
            pygame.init()

            # Screen dimensions
            info = pygame.display.Info()
            WIDTH, HEIGHT = info.current_w, info.current_h
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Interactive Math Roadmap")

            # Colors
            LIGHT_YELLOW = (255, 255, 204)
            DARK_YELLOW = (255, 204, 102)
            BROWN = (139, 69, 19)
            YELLOW = (255, 255, 0)
            ORANGE = (255, 165, 0)
            GOLD = (255, 215, 0)
            GRAY = (169, 169, 169)
            DARK_GRAY = (105, 105, 105)
            BLACK = (0, 0, 0)
            WINDOW_COLOR = (173, 216, 230)  # Light blue for windows
            TREE_GREEN = (34, 139, 34)
            TREE_BARK = (101, 67, 33)  # Brown for tree bark
            CLOUD_WHITE = (255, 255, 255)
            SKY_BLUE = (135, 206, 235)
            SIGN_COLOR = (255, 255, 255)
            SIGN_TEXT_COLOR = BLACK
            STICKMAN_COLOR = (0, 0, 0)

            # City positions and labels
            cities = [
                {"position": (WIDTH // 2 - 400, HEIGHT // 2 + 200), "label": "Start", "radius": 60},
                {"position": (WIDTH // 2 - 200, HEIGHT // 2 + 50), "label": "Level-1", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/A1.html"},
                {"position": (WIDTH // 2, HEIGHT // 2 - 100), "label": "Level-2", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/A2.html"},
                {"position": (WIDTH // 2 + 200, HEIGHT // 2 - 250), "label": "Level-3", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/A3.html"}
            ]

            # Road settings
            road_width = 60
            road_color = DARK_GRAY

            # Vehicle settings
            vehicle_width, vehicle_height = 50, 30
            vehicle_speed = 5

            # Load vehicle image and scale
            vehicle_image = pygame.Surface((vehicle_width, vehicle_height))
            vehicle_image.fill(YELLOW)
            # Add tiny boxes to represent car windows
            pygame.draw.rect(vehicle_image, BLACK, (5, 5, 10, 10))
            pygame.draw.rect(vehicle_image, BLACK, (35, 5, 10, 10))

            # Building settings
            building_width, building_height = 100, 120
            window_width, window_height = 20, 30  # Dimensions of windows
            building_gap = 20  # Gap between the road and buildings

            # Tree settings
            tree_width, tree_height = 50, 100
            tree_bark_width, tree_bark_height = 15, 30

            # FPS
            clock = pygame.time.Clock()
            FPS = 30

            # Dialogue box settings
            dialogue_font = pygame.font.Font(None, 32)
            dialogue_bg_color = DARK_YELLOW
            dialogue_text_color = BLACK
            dialogue_padding = 15
            dialogue_box_visible = False
            dialogue_content = ""
            dialogue_box_pos = (150, HEIGHT - 150)
            dialogue_box_size = (700, 120)

            # Game loop flag
            running = True
            exit_button_color = ORANGE
            exit_button_hover_color = YELLOW
            exit_button_text_color = BLACK
            exit_button_font = pygame.font.Font(None, 36)
            exit_button_pos = (WIDTH - 200, 50)
            exit_button_size = (150, 50)

            def draw_exit_button(hover=False):
                color = exit_button_hover_color if hover else exit_button_color
                pygame.draw.rect(screen, color, (*exit_button_pos, *exit_button_size))
                text = exit_button_font.render("Exit", True, exit_button_text_color)
                text_rect = text.get_rect(center=(exit_button_pos[0] + exit_button_size[0] // 2, exit_button_pos[1] + exit_button_size[1] // 2))
                screen.blit(text, text_rect)

            def is_mouse_over_exit_button(mouse_pos):
                return exit_button_pos[0] <= mouse_pos[0] <= exit_button_pos[0] + exit_button_size[0] and \
                    exit_button_pos[1] <= mouse_pos[1] <= exit_button_pos[1] + exit_button_size[1]

            def draw_road():
                for i in range(len(cities) - 1):
                    start_pos = cities[i]["position"]
                    end_pos = cities[i + 1]["position"]

                    # Calculate control points for a smoother curve
                    control_point1 = (start_pos[0] + (end_pos[0] - start_pos[0]) / 2, start_pos[1])
                    control_point2 = (end_pos[0] - (end_pos[0] - start_pos[0]) / 2, end_pos[1])

                    # Draw the curved road
                    pygame.draw.aalines(screen, road_color, False, [
                        start_pos,
                        control_point1,
                        control_point2,
                        end_pos
                    ], road_width)

            def draw_city(city, hover=False):
                color = GOLD if not hover else ORANGE
                pygame.draw.circle(screen, color, city["position"], city["radius"])
                font = pygame.font.Font(None, 40)
                text = font.render(city["label"], True, BLACK)
                text_rect = text.get_rect(center=city["position"])
                screen.blit(text, text_rect)

            def draw_buildings():
                building_positions = [
                    (WIDTH // 2 - 500, HEIGHT // 2 - 80),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 20),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 120)
                ]
                for pos in building_positions:
                    pygame.draw.rect(screen, BROWN, (*pos, building_width, building_height))
                    pygame.draw.polygon(screen, ORANGE, [
                        (pos[0], pos[1]),
                        (pos[0] + building_width, pos[1]),
                        (pos[0] + building_width // 2, pos[1] - 40)
                    ])
                    # Draw windows
                    window_pos = (pos[0] + 10, pos[1] + 20)
                    pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos, window_width, window_height))
                    pygame.draw.rect(screen, WINDOW_COLOR, (window_pos[0] + 30, window_pos[1], window_width, window_height))

                    # Duplicate building to the left of every landmark
                    for city in cities:
                        if pos[0] + building_width < city["position"][0] - 20:  # Ensure space between building and city
                            building_pos_left = (city["position"][0] - 2 * building_width - 60, city["position"][1] - building_height // 2)
                            pygame.draw.rect(screen, BROWN, (*building_pos_left, building_width, building_height))
                            pygame.draw.polygon(screen, ORANGE, [
                                (building_pos_left[0], building_pos_left[1]),
                                (building_pos_left[0] + building_width, building_pos_left[1]),
                                (building_pos_left[0] + building_width // 2, building_pos_left[1] - 40)
                            ])
                            # Draw windows
                            window_pos_left = (building_pos_left[0] + 10, building_pos_left[1] + 20)
                            pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos_left, window_width, window_height))
                            pygame.draw.rect(screen, WINDOW_COLOR, (window_pos_left[0] + 30, window_pos_left[1], window_width, window_height))

            def draw_trees():
                tree_positions = [
                    (WIDTH // 2 + 400 - 80, HEIGHT // 2 + 80),
                    (WIDTH // 2 + 400 + 80, HEIGHT // 2 + 80)
                ]
                for pos in tree_positions:
                    pygame.draw.rect(screen, TREE_BARK, (pos[0] + 10, pos[1] + 30, tree_bark_width, tree_bark_height))
                    pygame.draw.rect(screen, TREE_GREEN, (*pos, tree_width, tree_height))
                    pygame.draw.polygon(screen, TREE_GREEN, [
                        (pos[0] - 20, pos[1]),
                        (pos[0] + 70, pos[1]),
                        (pos[0] + 25, pos[1] - 50)
                    ])

            def draw_sky_and_clouds():
                # Draw the sky background
                pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT * 3 // 4))

                # Draw the ground background
                pygame.draw.rect(screen, DARK_YELLOW, (0, HEIGHT * 3 // 4, WIDTH, HEIGHT // 4))

                # Draw the clouds
                cloud_positions = [
                    (50, 50), (150, 100), (250, 50)
                ]
                for pos in cloud_positions:
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (*pos, 100, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 40, pos[1] - 20, 120, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 80, pos[1], 100, 60))

            def draw_stickman():
                stickman_pos = (WIDTH // 2 + 400, HEIGHT // 2 + 150)
                pygame.draw.circle(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 40), 20)  # Head
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0], stickman_pos[1] + 40), 5)  # Body
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] - 30, stickman_pos[1] + 30), 5)  # Left leg
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] + 30, stickman_pos[1] + 30), 5)  # Right leg
                pygame.draw.line(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 20), (stickman_pos[0] + 40, stickman_pos[1] - 20), 5)  # Right arm holding the sign
                pygame.draw.rect(screen, SIGN_COLOR, (stickman_pos[0] + 40, stickman_pos[1] - 70, 120, 50))  # Signboard
                font = pygame.font.Font(None, 30)
                text = font.render("Addition", True, SIGN_TEXT_COLOR)
                text_rect = text.get_rect(center=(stickman_pos[0] + 100, stickman_pos[1] - 45))
                screen.blit(text, text_rect)

            def draw_dialogue_box():
                if dialogue_box_visible:
                    pygame.draw.rect(screen, dialogue_bg_color, (*dialogue_box_pos, *dialogue_box_size))
                    pygame.draw.rect(screen, BLACK, (*dialogue_box_pos, *dialogue_box_size), 2)  # Border
                    dialogue_text = dialogue_font.render(dialogue_content, True, dialogue_text_color)
                    screen.blit(dialogue_text, (dialogue_box_pos[0] + dialogue_padding, dialogue_box_pos[1] + dialogue_padding))
            while running:
                screen.fill(LIGHT_YELLOW)

                draw_sky_and_clouds()
                draw_road()
                for city in cities:
                    draw_city(city)
                draw_buildings()
                draw_trees()
                draw_stickman()
                draw_dialogue_box()

                mouse_pos = pygame.mouse.get_pos()
                draw_exit_button(is_mouse_over_exit_button(mouse_pos))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if is_mouse_over_exit_button(mouse_pos):
                            running = False
                        else:
                            # Check if the mouse click is inside any city circle
                            for city in cities:
                                city_pos = city["position"]
                                distance = math.sqrt((mouse_pos[0] - city_pos[0]) ** 2 + (mouse_pos[1] - city_pos[1]) ** 2)
                                if distance <= city["radius"]:
                                    # Open the associated URL
                                    webbrowser.open(city.get("url"))
                                    break  # Exit the loop once a city is clicked

                pygame.display.update()
                clock.tick(FPS)

            # Quit Pygame
            pygame.quit()

        def subtraction():
            import pygame
            import math
            import webbrowser
            # Initialize Pygame
            pygame.init()

            # Screen dimensions
            info = pygame.display.Info()
            WIDTH, HEIGHT = info.current_w, info.current_h
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Interactive Math Roadmap")

            # Colors
            LIGHT_YELLOW = (255, 255, 204)
            DARK_YELLOW = (255, 204, 102)
            BROWN = (139, 69, 19)
            YELLOW = (255, 255, 0)
            ORANGE = (255, 165, 0)
            GOLD = (255, 215, 0)
            GRAY = (169, 169, 169)
            DARK_GRAY = (105, 105, 105)
            BLACK = (0, 0, 0)
            WINDOW_COLOR = (173, 216, 230)  # Light blue for windows
            TREE_GREEN = (34, 139, 34)
            TREE_BARK = (101, 67, 33)  # Brown for tree bark
            CLOUD_WHITE = (255, 255, 255)
            SKY_BLUE = (135, 206, 235)
            SIGN_COLOR = (255, 255, 255)
            SIGN_TEXT_COLOR = BLACK
            STICKMAN_COLOR = (0, 0, 0)

            # City positions and labels
            cities = [
                {"position": (WIDTH // 2 - 400, HEIGHT // 2 + 200), "label": "Start", "radius": 60},
                {"position": (WIDTH // 2 - 200, HEIGHT // 2 + 50), "label": "Level-1", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/S1.html"},
                {"position": (WIDTH // 2, HEIGHT // 2 - 100), "label": "Level-2", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/S2.html"},
                {"position": (WIDTH // 2 + 200, HEIGHT // 2 - 250), "label": "Level-3", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/S3.html"}
            ]

            # Road settings
            road_width = 60
            road_color = DARK_GRAY

            # Vehicle settings
            vehicle_width, vehicle_height = 50, 30
            vehicle_speed = 5

            # Load vehicle image and scale
            vehicle_image = pygame.Surface((vehicle_width, vehicle_height))
            vehicle_image.fill(YELLOW)
            # Add tiny boxes to represent car windows
            pygame.draw.rect(vehicle_image, BLACK, (5, 5, 10, 10))
            pygame.draw.rect(vehicle_image, BLACK, (35, 5, 10, 10))

            # Building settings
            building_width, building_height = 100, 120
            window_width, window_height = 20, 30  # Dimensions of windows
            building_gap = 20  # Gap between the road and buildings

            # Tree settings
            tree_width, tree_height = 50, 100
            tree_bark_width, tree_bark_height = 15, 30

            # FPS
            clock = pygame.time.Clock()
            FPS = 30

            # Dialogue box settings
            dialogue_font = pygame.font.Font(None, 32)
            dialogue_bg_color = DARK_YELLOW
            dialogue_text_color = BLACK
            dialogue_padding = 15
            dialogue_box_visible = False
            dialogue_content = ""
            dialogue_box_pos = (150, HEIGHT - 150)
            dialogue_box_size = (700, 120)

            # Game loop flag
            running = True
            exit_button_color = ORANGE
            exit_button_hover_color = YELLOW
            exit_button_text_color = BLACK
            exit_button_font = pygame.font.Font(None, 36)
            exit_button_pos = (WIDTH - 200, 50)
            exit_button_size = (150, 50)

            def draw_exit_button(hover=False):
                color = exit_button_hover_color if hover else exit_button_color
                pygame.draw.rect(screen, color, (*exit_button_pos, *exit_button_size))
                text = exit_button_font.render("Exit", True, exit_button_text_color)
                text_rect = text.get_rect(center=(exit_button_pos[0] + exit_button_size[0] // 2, exit_button_pos[1] + exit_button_size[1] // 2))
                screen.blit(text, text_rect)

            def is_mouse_over_exit_button(mouse_pos):
                return exit_button_pos[0] <= mouse_pos[0] <= exit_button_pos[0] + exit_button_size[0] and \
                    exit_button_pos[1] <= mouse_pos[1] <= exit_button_pos[1] + exit_button_size[1]

            def draw_road():
                for i in range(len(cities) - 1):
                    start_pos = cities[i]["position"]
                    end_pos = cities[i + 1]["position"]

                    # Calculate control points for a smoother curve
                    control_point1 = (start_pos[0] + (end_pos[0] - start_pos[0]) / 2, start_pos[1])
                    control_point2 = (end_pos[0] - (end_pos[0] - start_pos[0]) / 2, end_pos[1])

                    # Draw the curved road
                    pygame.draw.aalines(screen, road_color, False, [
                        start_pos,
                        control_point1,
                        control_point2,
                        end_pos
                    ], road_width)

            def draw_city(city, hover=False):
                color = GOLD if not hover else ORANGE
                pygame.draw.circle(screen, color, city["position"], city["radius"])
                font = pygame.font.Font(None, 40)
                text = font.render(city["label"], True, BLACK)
                text_rect = text.get_rect(center=city["position"])
                screen.blit(text, text_rect)

            def draw_buildings():
                building_positions = [
                    (WIDTH // 2 - 500, HEIGHT // 2 - 80),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 20),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 120)
                ]
                for pos in building_positions:
                    pygame.draw.rect(screen, BROWN, (*pos, building_width, building_height))
                    pygame.draw.polygon(screen, ORANGE, [
                        (pos[0], pos[1]),
                        (pos[0] + building_width, pos[1]),
                        (pos[0] + building_width // 2, pos[1] - 40)
                    ])
                    # Draw windows
                    window_pos = (pos[0] + 10, pos[1] + 20)
                    pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos, window_width, window_height))
                    pygame.draw.rect(screen, WINDOW_COLOR, (window_pos[0] + 30, window_pos[1], window_width, window_height))

                    # Duplicate building to the left of every landmark
                    for city in cities:
                        if pos[0] + building_width < city["position"][0] - 20:  # Ensure space between building and city
                            building_pos_left = (city["position"][0] - 2 * building_width - 60, city["position"][1] - building_height // 2)
                            pygame.draw.rect(screen, BROWN, (*building_pos_left, building_width, building_height))
                            pygame.draw.polygon(screen, ORANGE, [
                                (building_pos_left[0], building_pos_left[1]),
                                (building_pos_left[0] + building_width, building_pos_left[1]),
                                (building_pos_left[0] + building_width // 2, building_pos_left[1] - 40)
                            ])
                            # Draw windows
                            window_pos_left = (building_pos_left[0] + 10, building_pos_left[1] + 20)
                            pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos_left, window_width, window_height))
                            pygame.draw.rect(screen, WINDOW_COLOR, (window_pos_left[0] + 30, window_pos_left[1], window_width, window_height))

            def draw_trees():
                tree_positions = [
                    (WIDTH // 2 + 400 - 80, HEIGHT // 2 + 80),
                    (WIDTH // 2 + 400 + 80, HEIGHT // 2 + 80)
                ]
                for pos in tree_positions:
                    pygame.draw.rect(screen, TREE_BARK, (pos[0] + 10, pos[1] + 30, tree_bark_width, tree_bark_height))
                    pygame.draw.rect(screen, TREE_GREEN, (*pos, tree_width, tree_height))
                    pygame.draw.polygon(screen, TREE_GREEN, [
                        (pos[0] - 20, pos[1]),
                        (pos[0] + 70, pos[1]),
                        (pos[0] + 25, pos[1] - 50)
                    ])

            def draw_sky_and_clouds():
                # Draw the sky background
                pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT * 3 // 4))

                # Draw the ground background
                pygame.draw.rect(screen, DARK_YELLOW, (0, HEIGHT * 3 // 4, WIDTH, HEIGHT // 4))

                # Draw the clouds
                cloud_positions = [
                    (50, 50), (150, 100), (250, 50)
                ]
                for pos in cloud_positions:
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (*pos, 100, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 40, pos[1] - 20, 120, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 80, pos[1], 100, 60))

            def draw_stickman():
                stickman_pos = (WIDTH // 2 + 400, HEIGHT // 2 + 150)
                pygame.draw.circle(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 40), 20)  # Head
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0], stickman_pos[1] + 40), 5)  # Body
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] - 30, stickman_pos[1] + 30), 5)  # Left leg
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] + 30, stickman_pos[1] + 30), 5)  # Right leg
                pygame.draw.line(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 20), (stickman_pos[0] + 40, stickman_pos[1] - 20), 5)  # Right arm holding the sign
                pygame.draw.rect(screen, SIGN_COLOR, (stickman_pos[0] + 40, stickman_pos[1] - 70, 120, 50))  # Signboard
                font = pygame.font.Font(None, 30)
                text = font.render("Subtraction", True, SIGN_TEXT_COLOR)
                text_rect = text.get_rect(center=(stickman_pos[0] + 100, stickman_pos[1] - 45))
                screen.blit(text, text_rect)

            def draw_dialogue_box():
                if dialogue_box_visible:
                    pygame.draw.rect(screen, dialogue_bg_color, (*dialogue_box_pos, *dialogue_box_size))
                    pygame.draw.rect(screen, BLACK, (*dialogue_box_pos, *dialogue_box_size), 2)  # Border
                    dialogue_text = dialogue_font.render(dialogue_content, True, dialogue_text_color)
                    screen.blit(dialogue_text, (dialogue_box_pos[0] + dialogue_padding, dialogue_box_pos[1] + dialogue_padding))
            # Main game loop
            while running:
                screen.fill(LIGHT_YELLOW)

                draw_sky_and_clouds()
                draw_road()
                for city in cities:
                    draw_city(city)
                draw_buildings()
                draw_trees()
                draw_stickman()
                draw_dialogue_box()

                mouse_pos = pygame.mouse.get_pos()
                draw_exit_button(is_mouse_over_exit_button(mouse_pos))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if is_mouse_over_exit_button(mouse_pos):
                            running = False
                        else:
                            # Check if the mouse click is inside any city circle
                            for city in cities:
                                city_pos = city["position"]
                                distance = math.sqrt((mouse_pos[0] - city_pos[0]) ** 2 + (mouse_pos[1] - city_pos[1]) ** 2)
                                if distance <= city["radius"]:
                                    # Open the associated URL
                                    webbrowser.open(city.get("url"))
                                    break  # Exit the loop once a city is clicked

                pygame.display.update()
                clock.tick(FPS)

            # Quit Pygame
            pygame.quit()

        def multiplication():
            import pygame
            import math
            import webbrowser
            # Initialize Pygame
            pygame.init()

            # Screen dimensions
            info = pygame.display.Info()
            WIDTH, HEIGHT = info.current_w, info.current_h
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Interactive Math Roadmap")

            # Colors
            LIGHT_YELLOW = (255, 255, 204)
            DARK_YELLOW = (255, 204, 102)
            BROWN = (139, 69, 19)
            YELLOW = (255, 255, 0)
            ORANGE = (255, 165, 0)
            GOLD = (255, 215, 0)
            GRAY = (169, 169, 169)
            DARK_GRAY = (105, 105, 105)
            BLACK = (0, 0, 0)
            WINDOW_COLOR = (173, 216, 230)  # Light blue for windows
            TREE_GREEN = (34, 139, 34)
            TREE_BARK = (101, 67, 33)  # Brown for tree bark
            CLOUD_WHITE = (255, 255, 255)
            SKY_BLUE = (135, 206, 235)
            SIGN_COLOR = (255, 255, 255)
            SIGN_TEXT_COLOR = BLACK
            STICKMAN_COLOR = (0, 0, 0)

            # City positions and labels
            cities = [
                {"position": (WIDTH // 2 - 400, HEIGHT // 2 + 200), "label": "Start", "radius": 60},
                {"position": (WIDTH // 2 - 200, HEIGHT // 2 + 50), "label": "Level-1", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/M1.html"},
                {"position": (WIDTH // 2, HEIGHT // 2 - 100), "label": "Level-2", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/M2.html"},
                {"position": (WIDTH // 2 + 200, HEIGHT // 2 - 250), "label": "Level-3", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/M3.html"}
            ]

            # Road settings
            road_width = 60
            road_color = DARK_GRAY

            # Vehicle settings
            vehicle_width, vehicle_height = 50, 30
            vehicle_speed = 5

            # Load vehicle image and scale
            vehicle_image = pygame.Surface((vehicle_width, vehicle_height))
            vehicle_image.fill(YELLOW)
            # Add tiny boxes to represent car windows
            pygame.draw.rect(vehicle_image, BLACK, (5, 5, 10, 10))
            pygame.draw.rect(vehicle_image, BLACK, (35, 5, 10, 10))

            # Building settings
            building_width, building_height = 100, 120
            window_width, window_height = 20, 30  # Dimensions of windows
            building_gap = 20  # Gap between the road and buildings

            # Tree settings
            tree_width, tree_height = 50, 100
            tree_bark_width, tree_bark_height = 15, 30

            # FPS
            clock = pygame.time.Clock()
            FPS = 30

            # Dialogue box settings
            dialogue_font = pygame.font.Font(None, 32)
            dialogue_bg_color = DARK_YELLOW
            dialogue_text_color = BLACK
            dialogue_padding = 15
            dialogue_box_visible = False
            dialogue_content = ""
            dialogue_box_pos = (150, HEIGHT - 150)
            dialogue_box_size = (700, 120)

            # Game loop flag
            running = True
            exit_button_color = ORANGE
            exit_button_hover_color = YELLOW
            exit_button_text_color = BLACK
            exit_button_font = pygame.font.Font(None, 36)
            exit_button_pos = (WIDTH - 200, 50)
            exit_button_size = (150, 50)

            def draw_exit_button(hover=False):
                color = exit_button_hover_color if hover else exit_button_color
                pygame.draw.rect(screen, color, (*exit_button_pos, *exit_button_size))
                text = exit_button_font.render("Exit", True, exit_button_text_color)
                text_rect = text.get_rect(center=(exit_button_pos[0] + exit_button_size[0] // 2, exit_button_pos[1] + exit_button_size[1] // 2))
                screen.blit(text, text_rect)

            def is_mouse_over_exit_button(mouse_pos):
                return exit_button_pos[0] <= mouse_pos[0] <= exit_button_pos[0] + exit_button_size[0] and \
                    exit_button_pos[1] <= mouse_pos[1] <= exit_button_pos[1] + exit_button_size[1]

            def draw_road():
                for i in range(len(cities) - 1):
                    start_pos = cities[i]["position"]
                    end_pos = cities[i + 1]["position"]

                    # Calculate control points for a smoother curve
                    control_point1 = (start_pos[0] + (end_pos[0] - start_pos[0]) / 2, start_pos[1])
                    control_point2 = (end_pos[0] - (end_pos[0] - start_pos[0]) / 2, end_pos[1])

                    # Draw the curved road
                    pygame.draw.aalines(screen, road_color, False, [
                        start_pos,
                        control_point1,
                        control_point2,
                        end_pos
                    ], road_width)

            def draw_city(city, hover=False):
                color = GOLD if not hover else ORANGE
                pygame.draw.circle(screen, color, city["position"], city["radius"])
                font = pygame.font.Font(None, 40)
                text = font.render(city["label"], True, BLACK)
                text_rect = text.get_rect(center=city["position"])
                screen.blit(text, text_rect)

            def draw_buildings():
                building_positions = [
                    (WIDTH // 2 - 500, HEIGHT // 2 - 80),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 20),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 120)
                ]
                for pos in building_positions:
                    pygame.draw.rect(screen, BROWN, (*pos, building_width, building_height))
                    pygame.draw.polygon(screen, ORANGE, [
                        (pos[0], pos[1]),
                        (pos[0] + building_width, pos[1]),
                        (pos[0] + building_width // 2, pos[1] - 40)
                    ])
                    # Draw windows
                    window_pos = (pos[0] + 10, pos[1] + 20)
                    pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos, window_width, window_height))
                    pygame.draw.rect(screen, WINDOW_COLOR, (window_pos[0] + 30, window_pos[1], window_width, window_height))

                    # Duplicate building to the left of every landmark
                    for city in cities:
                        if pos[0] + building_width < city["position"][0] - 20:  # Ensure space between building and city
                            building_pos_left = (city["position"][0] - 2 * building_width - 60, city["position"][1] - building_height // 2)
                            pygame.draw.rect(screen, BROWN, (*building_pos_left, building_width, building_height))
                            pygame.draw.polygon(screen, ORANGE, [
                                (building_pos_left[0], building_pos_left[1]),
                                (building_pos_left[0] + building_width, building_pos_left[1]),
                                (building_pos_left[0] + building_width // 2, building_pos_left[1] - 40)
                            ])
                            # Draw windows
                            window_pos_left = (building_pos_left[0] + 10, building_pos_left[1] + 20)
                            pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos_left, window_width, window_height))
                            pygame.draw.rect(screen, WINDOW_COLOR, (window_pos_left[0] + 30, window_pos_left[1], window_width, window_height))

            def draw_trees():
                tree_positions = [
                    (WIDTH // 2 + 400 - 80, HEIGHT // 2 + 80),
                    (WIDTH // 2 + 400 + 80, HEIGHT // 2 + 80)
                ]
                for pos in tree_positions:
                    pygame.draw.rect(screen, TREE_BARK, (pos[0] + 10, pos[1] + 30, tree_bark_width, tree_bark_height))
                    pygame.draw.rect(screen, TREE_GREEN, (*pos, tree_width, tree_height))
                    pygame.draw.polygon(screen, TREE_GREEN, [
                        (pos[0] - 20, pos[1]),
                        (pos[0] + 70, pos[1]),
                        (pos[0] + 25, pos[1] - 50)
                    ])

            def draw_sky_and_clouds():
                # Draw the sky background
                pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT * 3 // 4))

                # Draw the ground background
                pygame.draw.rect(screen, DARK_YELLOW, (0, HEIGHT * 3 // 4, WIDTH, HEIGHT // 4))

                # Draw the clouds
                cloud_positions = [
                    (50, 50), (150, 100), (250, 50)
                ]
                for pos in cloud_positions:
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (*pos, 100, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 40, pos[1] - 20, 120, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 80, pos[1], 100, 60))

            def draw_stickman():
                stickman_pos = (WIDTH // 2 + 400, HEIGHT // 2 + 150)
                pygame.draw.circle(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 40), 20)  # Head
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0], stickman_pos[1] + 40), 5)  # Body
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] - 30, stickman_pos[1] + 30), 5)  # Left leg
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] + 30, stickman_pos[1] + 30), 5)  # Right leg
                pygame.draw.line(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 20), (stickman_pos[0] + 40, stickman_pos[1] - 20), 5)  # Right arm holding the sign
                pygame.draw.rect(screen, SIGN_COLOR, (stickman_pos[0] + 40, stickman_pos[1] - 70, 120, 50))  # Signboard
                font = pygame.font.Font(None, 30)
                text = font.render("Multiplication", True, SIGN_TEXT_COLOR)
                text_rect = text.get_rect(center=(stickman_pos[0] + 100, stickman_pos[1] - 45))
                screen.blit(text, text_rect)

            def draw_dialogue_box():
                if dialogue_box_visible:
                    pygame.draw.rect(screen, dialogue_bg_color, (*dialogue_box_pos, *dialogue_box_size))
                    pygame.draw.rect(screen, BLACK, (*dialogue_box_pos, *dialogue_box_size), 2)  # Border
                    dialogue_text = dialogue_font.render(dialogue_content, True, dialogue_text_color)
                    screen.blit(dialogue_text, (dialogue_box_pos[0] + dialogue_padding, dialogue_box_pos[1] + dialogue_padding))

            # Main game loop
           # Main game loop
            while running:
                screen.fill(LIGHT_YELLOW)

                draw_sky_and_clouds()
                draw_road()
                for city in cities:
                    draw_city(city)
                draw_buildings()
                draw_trees()
                draw_stickman()
                draw_dialogue_box()

                mouse_pos = pygame.mouse.get_pos()
                draw_exit_button(is_mouse_over_exit_button(mouse_pos))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if is_mouse_over_exit_button(mouse_pos):
                            running = False
                        else:
                            # Check if the mouse click is inside any city circle
                            for city in cities:
                                city_pos = city["position"]
                                distance = math.sqrt((mouse_pos[0] - city_pos[0]) ** 2 + (mouse_pos[1] - city_pos[1]) ** 2)
                                if distance <= city["radius"]:
                                    # Open the associated URL
                                    webbrowser.open(city.get("url"))
                                    break  # Exit the loop once a city is clicked

                pygame.display.update()
                clock.tick(FPS)

            # Quit Pygame
            pygame.quit()

        def division():
            import pygame
            import math
            import webbrowser
            # Initialize Pygame
            pygame.init()

            # Screen dimensions
            info = pygame.display.Info()
            WIDTH, HEIGHT = info.current_w, info.current_h
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Interactive Math Roadmap")

            # Colors
            LIGHT_YELLOW = (255, 255, 204)
            DARK_YELLOW = (255, 204, 102)
            BROWN = (139, 69, 19)
            YELLOW = (255, 255, 0)
            ORANGE = (255, 165, 0)
            GOLD = (255, 215, 0)
            GRAY = (169, 169, 169)
            DARK_GRAY = (105, 105, 105)
            BLACK = (0, 0, 0)
            WINDOW_COLOR = (173, 216, 230)  # Light blue for windows
            TREE_GREEN = (34, 139, 34)
            TREE_BARK = (101, 67, 33)  # Brown for tree bark
            CLOUD_WHITE = (255, 255, 255)
            SKY_BLUE = (135, 206, 235)
            SIGN_COLOR = (255, 255, 255)
            SIGN_TEXT_COLOR = BLACK
            STICKMAN_COLOR = (0, 0, 0)

            # City positions and labels
            cities = [
                {"position": (WIDTH // 2 - 400, HEIGHT // 2 + 200), "label": "Start", "radius": 60},
                {"position": (WIDTH // 2 - 200, HEIGHT // 2 + 50), "label": "Level-1", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/D1.html"},
                {"position": (WIDTH // 2, HEIGHT // 2 - 100), "label": "Level-2", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/D2.html"},
                {"position": (WIDTH // 2 + 200, HEIGHT // 2 - 250), "label": "Level-3", "radius": 70,"url":"https://andu.jaidrew.co.in/SIH/D3.html"}
            ]

            # Road settings
            road_width = 60
            road_color = DARK_GRAY

            # Vehicle settings
            vehicle_width, vehicle_height = 50, 30
            vehicle_speed = 5

            # Load vehicle image and scale
            vehicle_image = pygame.Surface((vehicle_width, vehicle_height))
            vehicle_image.fill(YELLOW)
            # Add tiny boxes to represent car windows
            pygame.draw.rect(vehicle_image, BLACK, (5, 5, 10, 10))
            pygame.draw.rect(vehicle_image, BLACK, (35, 5, 10, 10))

            # Building settings
            building_width, building_height = 100, 120
            window_width, window_height = 20, 30  # Dimensions of windows
            building_gap = 20  # Gap between the road and buildings

            # Tree settings
            tree_width, tree_height = 50, 100
            tree_bark_width, tree_bark_height = 15, 30

            # FPS
            clock = pygame.time.Clock()
            FPS = 30

            # Dialogue box settings
            dialogue_font = pygame.font.Font(None, 32)
            dialogue_bg_color = DARK_YELLOW
            dialogue_text_color = BLACK
            dialogue_padding = 15
            dialogue_box_visible = False
            dialogue_content = ""
            dialogue_box_pos = (150, HEIGHT - 150)
            dialogue_box_size = (700, 120)

            # Game loop flag
            running = True
            exit_button_color = ORANGE
            exit_button_hover_color = YELLOW
            exit_button_text_color = BLACK
            exit_button_font = pygame.font.Font(None, 36)
            exit_button_pos = (WIDTH - 200, 50)
            exit_button_size = (150, 50)

            def draw_exit_button(hover=False):
                color = exit_button_hover_color if hover else exit_button_color
                pygame.draw.rect(screen, color, (*exit_button_pos, *exit_button_size))
                text = exit_button_font.render("Exit", True, exit_button_text_color)
                text_rect = text.get_rect(center=(exit_button_pos[0] + exit_button_size[0] // 2, exit_button_pos[1] + exit_button_size[1] // 2))
                screen.blit(text, text_rect)

            def is_mouse_over_exit_button(mouse_pos):
                return exit_button_pos[0] <= mouse_pos[0] <= exit_button_pos[0] + exit_button_size[0] and \
                    exit_button_pos[1] <= mouse_pos[1] <= exit_button_pos[1] + exit_button_size[1]

            def draw_road():
                for i in range(len(cities) - 1):
                    start_pos = cities[i]["position"]
                    end_pos = cities[i + 1]["position"]

                    # Calculate control points for a smoother curve
                    control_point1 = (start_pos[0] + (end_pos[0] - start_pos[0]) / 2, start_pos[1])
                    control_point2 = (end_pos[0] - (end_pos[0] - start_pos[0]) / 2, end_pos[1])

                    # Draw the curved road
                    pygame.draw.aalines(screen, road_color, False, [
                        start_pos,
                        control_point1,
                        control_point2,
                        end_pos
                    ], road_width)

            def draw_city(city, hover=False):
                color = GOLD if not hover else ORANGE
                pygame.draw.circle(screen, color, city["position"], city["radius"])
                font = pygame.font.Font(None, 40)
                text = font.render(city["label"], True, BLACK)
                text_rect = text.get_rect(center=city["position"])
                screen.blit(text, text_rect)

            def draw_buildings():
                building_positions = [
                    (WIDTH // 2 - 500, HEIGHT // 2 - 80),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 20),
                    (WIDTH // 2 - 500, HEIGHT // 2 - 120)
                ]
                for pos in building_positions:
                    pygame.draw.rect(screen, BROWN, (*pos, building_width, building_height))
                    pygame.draw.polygon(screen, ORANGE, [
                        (pos[0], pos[1]),
                        (pos[0] + building_width, pos[1]),
                        (pos[0] + building_width // 2, pos[1] - 40)
                    ])
                    # Draw windows
                    window_pos = (pos[0] + 10, pos[1] + 20)
                    pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos, window_width, window_height))
                    pygame.draw.rect(screen, WINDOW_COLOR, (window_pos[0] + 30, window_pos[1], window_width, window_height))

                    # Duplicate building to the left of every landmark
                    for city in cities:
                        if pos[0] + building_width < city["position"][0] - 20:  # Ensure space between building and city
                            building_pos_left = (city["position"][0] - 2 * building_width - 60, city["position"][1] - building_height // 2)
                            pygame.draw.rect(screen, BROWN, (*building_pos_left, building_width, building_height))
                            pygame.draw.polygon(screen, ORANGE, [
                                (building_pos_left[0], building_pos_left[1]),
                                (building_pos_left[0] + building_width, building_pos_left[1]),
                                (building_pos_left[0] + building_width // 2, building_pos_left[1] - 40)
                            ])
                            # Draw windows
                            window_pos_left = (building_pos_left[0] + 10, building_pos_left[1] + 20)
                            pygame.draw.rect(screen, WINDOW_COLOR, (*window_pos_left, window_width, window_height))
                            pygame.draw.rect(screen, WINDOW_COLOR, (window_pos_left[0] + 30, window_pos_left[1], window_width, window_height))

            def draw_trees():
                tree_positions = [
                    (WIDTH // 2 + 400 - 80, HEIGHT // 2 + 80),
                    (WIDTH // 2 + 400 + 80, HEIGHT // 2 + 80)
                ]
                for pos in tree_positions:
                    pygame.draw.rect(screen, TREE_BARK, (pos[0] + 10, pos[1] + 30, tree_bark_width, tree_bark_height))
                    pygame.draw.rect(screen, TREE_GREEN, (*pos, tree_width, tree_height))
                    pygame.draw.polygon(screen, TREE_GREEN, [
                        (pos[0] - 20, pos[1]),
                        (pos[0] + 70, pos[1]),
                        (pos[0] + 25, pos[1] - 50)
                    ])

            def draw_sky_and_clouds():
                # Draw the sky background
                pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT * 3 // 4))

                # Draw the ground background
                pygame.draw.rect(screen, DARK_YELLOW, (0, HEIGHT * 3 // 4, WIDTH, HEIGHT // 4))

                # Draw the clouds
                cloud_positions = [
                    (50, 50), (150, 100), (250, 50)
                ]
                for pos in cloud_positions:
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (*pos, 100, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 40, pos[1] - 20, 120, 60))
                    pygame.draw.ellipse(screen, CLOUD_WHITE, (pos[0] + 80, pos[1], 100, 60))

            def draw_stickman():
                stickman_pos = (WIDTH // 2 + 400, HEIGHT // 2 + 150)
                pygame.draw.circle(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 40), 20)  # Head
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0], stickman_pos[1] + 40), 5)  # Body
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] - 30, stickman_pos[1] + 30), 5)  # Left leg
                pygame.draw.line(screen, STICKMAN_COLOR, stickman_pos, (stickman_pos[0] + 30, stickman_pos[1] + 30), 5)  # Right leg
                pygame.draw.line(screen, STICKMAN_COLOR, (stickman_pos[0], stickman_pos[1] - 20), (stickman_pos[0] + 40, stickman_pos[1] - 20), 5)  # Right arm holding the sign
                pygame.draw.rect(screen, SIGN_COLOR, (stickman_pos[0] + 40, stickman_pos[1] - 70, 120, 50))  # Signboard
                font = pygame.font.Font(None, 30)
                text = font.render("Divison", True, SIGN_TEXT_COLOR)
                text_rect = text.get_rect(center=(stickman_pos[0] + 100, stickman_pos[1] - 45))
                screen.blit(text, text_rect)

            def draw_dialogue_box():
                if dialogue_box_visible:
                    pygame.draw.rect(screen, dialogue_bg_color, (*dialogue_box_pos, *dialogue_box_size))
                    pygame.draw.rect(screen, BLACK, (*dialogue_box_pos, *dialogue_box_size), 2)  # Border
                    dialogue_text = dialogue_font.render(dialogue_content, True, dialogue_text_color)
                    screen.blit(dialogue_text, (dialogue_box_pos[0] + dialogue_padding, dialogue_box_pos[1] + dialogue_padding))

            # Main game loop
            while running:
                screen.fill(LIGHT_YELLOW)

                draw_sky_and_clouds()
                draw_road()
                for city in cities:
                    draw_city(city)
                draw_buildings()
                draw_trees()
                draw_stickman()
                draw_dialogue_box()

                mouse_pos = pygame.mouse.get_pos()
                draw_exit_button(is_mouse_over_exit_button(mouse_pos))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if is_mouse_over_exit_button(mouse_pos):
                            running = False

                pygame.display.update()
                clock.tick(FPS)

            # Quit Pygame
            pygame.quit()

        # Create the main window
        root = tk.Tk()
        root.title("Math Operations Dashboard")
        root.geometry("400x400")

        # Heading label
        heading = tk.Label(root, text="You Have Selected Learn Maps \n Click on one of the four Learn Maps ", font=("Helvetica", 16))
        heading.pack(pady=20)

        # Button for Addition
        addition_button = tk.Button(root, text="Addition", font=("Helvetica", 14), width=15, height=2, command=addition)
        addition_button.pack(pady=10)

        # Button for Subtraction
        subtraction_button = tk.Button(root, text="Subtraction", font=("Helvetica", 14), width=15, height=2, command=subtraction)
        subtraction_button.pack(pady=10)

        # Button for Multiplication
        multiplication_button = tk.Button(root, text="Multiplication", font=("Helvetica", 14), width=15, height=2, command=multiplication)
        multiplication_button.pack(pady=10)

        # Button for Division (this will launch the Pygame window)
        division_button = tk.Button(root, text="Division", font=("Helvetica", 14), width=15, height=2, command=division)
        division_button.pack(pady=10)

        # Start the Tkinter main loop
        root.mainloop()


    def reading_quiz():
        webbrowser.open("https://www.example.com")

    # Buttons for the Maths GUI
    learn_maps_button = tk.Button(maths_window, text="Learn Maps", command=learn_maps,
                                  bg="#008CBA", fg="white", font=("Arial", 12))
    learn_maps_button.pack(pady=10)

    reading_quiz_button = tk.Button(maths_window, text="Reading Quiz", command=reading_quiz,
                                    bg="#4CAF50", fg="white", font=("Arial", 12))
    reading_quiz_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Simba's Learning Safari")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Heading label
heading = tk.Label(root, text="Welcome to Simba's Learning Safari \nChoose where you need to go:", font=("Helvetica", 16),
                  bg="#f0f0f0", fg="#333333")
heading.pack(pady=20)

# Button for Dashboard
dashboard_button = tk.Button(root, text="Dashboard", font=("Arial", 12), width=15, height=2, command=dashboard,
                            bg="#008CBA", fg="white")
dashboard_button.pack(pady=10)

# Button for Maths Course (opens a new window)
maths_button = tk.Button(root, text="Maths Course", font=("Arial", 12), width=15, height=2, command=open_maths_gui,
                        bg="#4CAF50", fg="white")
maths_button.pack(pady=10)

# Button for Science Course
science_button = tk.Button(root, text="Science Course", font=("Arial", 12), width=15, height=2, command=science_course,
                           bg="#f44336", fg="white")
science_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()