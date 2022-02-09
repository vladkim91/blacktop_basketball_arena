export default [
  {
    name: 'Michael Jordan',
    nickname: 'Air Jordan',
    height: `6'6"`,
    avatar: 'img/url',
    description: `Michael Jordan personified greatness on the court, and redefined superstar athlete off it. His freshman season at UNC culminated with Jordan hitting the game-winning shot in the 1982 NCAA national title game. That shot put Michael on the map and a new era was born. Following his junior year, Jordan entered the NBA Draft and was selected third overall by the Chicago Bulls. The young superstar began stockpiling NBA hardware. The court was his and the world soon followed. His unmistakable style - the wagging tongue, the baggy shorts, the signature line of sneakers - helped make the 14-time All Star the most recognizable person on the planet. Still his resume lacked an NBA title. Then in 1991, the Jordan-led Bulls launched an all-out assault on the rest of the league winning three straight world championships. Michael won Olympic gold again in 1992 and then in 1993 abruptly retired from the Bulls to play minor league baseball. He returned to the NBA full-time in 1995 and the Bulls promptly won three consecutive titles. Jordan was named Finals MVP each time. In 2001, Jordan made a second improbable comeback and still averaged 20 points per game and appeared in the 2002 and 2003 All Star Games.`,
    attributes: {
      offense: {
        layup: 95,
        dunk: 99,
        mid_range: 95,
        three: 80,
        handles: 90,
        pass: 87,
        off_rebound: 65,
        post_shot: 70
      },
      defense: {
        inside_defense: 75,
        outside_defense: 95,
        steal: 87,
        block: 75,
        def_rebound: 70,
        post_defense: 75
      },
      physical: {
        speed: 95,
        vertical: 90,
        strength: 82
      }
    },
    tendencies: {
      offense: {
        attack_rim: 90,
        shoot_mid: 95,
        shoot_three: 60,
        pass: 60,
        set_screen: 40,
        post_up: 75
      },
      defense: {
        steal: 85,
        block: 70,
        hard_foul: 40,
        intercept: 80
      }
    }
  },
  {
    name: 'Tim Duncan',
    nickname: 'Big Fundamental',
    height: `6'11"`,
    avatar: 'img/url',
    description: `Timothy Theodore Duncan is an American former professional basketball player and coach. Nicknamed "the Big Fundamental", he is widely regarded as the greatest power forward of all time and one of the greatest players in NBA history. He spent his entire 19-year playing career with the San Antonio Spurs.`,
    attributes: {
      offense: {
        layup: 95,
        dunk: 95,
        mid_range: 80,
        three: 60,
        handles: 75,
        pass: 90,
        off_rebound: 95,
        post_shot: 95
      },
      defense: {
        inside_defense: 99,
        outside_defense: 75,
        steal: 80,
        block: 95,
        def_rebound: 95,
        post_defense: 95
      },
      physical: {
        speed: 65,
        vertical: 65,
        strength: 95
      }
    },
    tendencies: {
      offense: {
        attack_rim: 75,
        shoot_mid: 95,
        shoot_three: 30,
        pass: 60,
        set_screen: 90,
        post_up: 95
      },
      defense: {
        steal: 65,
        block: 87,
        hard_foul: 20,
        intercept: 60
      }
    }
  }
];
