import click

from enums import Strategies
from epsilon_greedy import epsilon_greedy_dice_num
from thompson_sampling import thompson_sampling_dice_num


@click.group()
def cli():
    pass


@click.command('start-player')
@click.option('--strategy', type=str, default='thompson_sampling')
def start_player_emulator(strategy: str):
    match strategy:
        case Strategies.epsilon_greedy.value:
            click.echo(f'Epsilon greedy optimal dice num: {epsilon_greedy_dice_num()}')
        case Strategies.thompson_sampling.value:
            click.echo(f'Thompson sampling optimal dice num: {thompson_sampling_dice_num()}')
        case Strategies.all.value:
            thompson_dice_num = thompson_sampling_dice_num()
            epsilon_dice_num = epsilon_greedy_dice_num()
            click.echo(f'Thompson sampling optimal dice num: {thompson_dice_num}')
            click.echo(f'Epsilon greedy optimal dice num: {epsilon_dice_num}')
        case _:
            click.echo(f'Unknown strategy: {strategy}')


cli.add_command(start_player_emulator)


if __name__ == '__main__':
    cli()
