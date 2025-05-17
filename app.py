from flask import Flask, render_template
import chess.pgn
import io

app = Flask(__name__)

@app.route('/')
def home():
    # Sample PGN string - note the formatting without indentation
    pgn_text = """[Event "Example Game"]
[Site "Internet Chess Club"]
[Date "2023.01.01"]
[White "Player1"]
[Black "Player2"]
[Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This is the Ruy Lopez} 4. Ba4 Nf6 5. O-O"""
    
    # Parse PGN
    pgn = io.StringIO(pgn_text)
    game = chess.pgn.read_game(pgn)
    
    # Extract basic info
    headers = dict(game.headers)
    print("Headers:", headers)  # Debug print
    
    # Get main line moves
    board = chess.Board()  # Corrected: Board with capital B
    moves = []
    
    for move in game.mainline_moves():
        moves.append(board.san(move))
        board.push(move)
    
    print("Moves:", moves)
    
    return render_template('index.html', 
                          message="PGN Test Successful!", 
                          game_info=headers,
                          moves=moves)

if __name__ == '__main__':
    app.run(debug=True)