from flask import Flask, jsonify, request

from entities import Dices


app = Flask(__name__)
dices = Dices('probability_distributions.json')


@app.route('/', methods=['GET'])
def root():
    return jsonify('Welcome to our casino!')


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(200)


@app.route('/get-realization', methods=['GET'])
def get_realization():
    dice_num = int(request.args.get('dice_num'))
    try:
        app.logger.info(f'User request dice with num: {dice_num}')
        realization = dices.generate_sample(dice_num=dice_num)
        app.logger.info(f'User get realization: {realization}')
    except ValueError:
        return jsonify({'error': f'Not a valid dice num: {dice_num}'})
    except KeyError:
        return jsonify({'error': f'Not existing dice with num: {dice_num}'})

    return jsonify({'realization': realization})


def main(host: str, port: int, debug: bool) -> None:
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main(host='0.0.0.0', port=5432, debug=True)
