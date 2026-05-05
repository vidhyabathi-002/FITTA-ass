# Space Shooter Game 🚀

A fun and creative **space invaders-style game** built with Pygame!

## Game Features
✨ **Player aircraft PNG sprite** that shoots enemies
✨ **Multiple enemy waves** with increasing difficulty
✨ **Enemy bullets** that damage the player
✨ **Power-ups** dropped by destroyed enemies
✨ **Score system** and wave progression
✨ **Lives system** - lose 3 lives and it's game over
✨ **Dynamic difficulty** - enemies spawn faster as you progress
✨ **Space background PNG** behind the action

## How to Run

1. **Make sure the venv is activated:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Run the game:**
   ```powershell
   python space_shooter.py
   ```

## Game Controls
| Key | Action |
|-----|--------|
| **← →** | Move spaceship left/right |
| **SPACE** | Shoot bullets |
| **R** | Restart game (when game over) |
| **Q** | Quit game (when game over) |

## Game Mechanics

- **Score**: Destroy enemies (+10 points), collect power-ups (+50 points)
- **Lives**: Start with 3 lives. Get hit by enemy bullets to lose a life
- **Waves**: Complete waves by destroying all spawned enemies
- **Difficulty**: Each wave spawns enemies faster!
- **Power-ups**: Green squares dropped by enemies - collect for bonus points

## Gameplay Tips
🎯 Stay in the center to have more mobility
🎯 Destroy enemies quickly before they reach you
🎯 Collect green power-ups for extra points
🎯 Each wave is harder - enemies spawn faster!

## Customization Ideas
- Replace `assets/player_aircraft.png` or `assets/enemy_aircraft.png` to customize sprites
- Replace `assets/space_background.png` to customize the background
- Change colors in the color variables for bullets, UI, and power-ups
- Adjust `enemy_spawn_rate` to change difficulty
- Add sound effects with pygame.mixer
- Add particle effects for explosions
- Create new power-up types
