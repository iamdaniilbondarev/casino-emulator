from flask import Flask, jsonify, request

from dice_emulator.entities import Dices
from dice_emulator.settings import PROBABILITY_FILE_PATH

app = Flask(__name__)
dices = Dices(PROBABILITY_FILE_PATH)


@app.route('/', methods=['GET'])
def root():
    return jsonify('Welcome to our casino!')


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(200)


@app.route('/get-realization', methods=['GET'])
def get_realization():
    dice_num = request.args.get('dice_num')
    try:
        dice_num_int = int(dice_num)
        app.logger.info(f'User request dice with num: {dice_num_int}')
        realization = dices.generate_sample(dice_num=dice_num_int)
        app.logger.info(f'User get realization: {realization}')
    except ValueError as exc:
        return jsonify({'error': f'Not a valid dice num: {dice_num}'})
    except KeyError as exc:
        return jsonify({'error': f'Not existing dice with num: {dice_num}'})

    return jsonify({'realization': realization})


if __name__ == '__main__':
    app.run(debug=True)
