#include <SFML/Graphics.hpp>
#include <optional>

int main(void)
{
    sf::RenderWindow window(sf::VideoMode({200, 200}), "SFML works!");
    sf::CircleShape shape(100.f);
    shape.setFillColor(sf::Color::Green);

    sf::Event event;
    
    while (window.isOpen())
    {
        // while (const std::optional event = window.pollEvent())
        while (window.pollEvent(event))
        {
            // if (event->is<sf::Event::Closed>())
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();
    }

    return 0;
}