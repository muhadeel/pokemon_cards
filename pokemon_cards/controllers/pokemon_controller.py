from flask import render_template, request, redirect, url_for, Blueprint

from pokemon_cards.components.pokemon_component import PokemonComponent

pokemons_bp = Blueprint('pokemons', __name__)


@pokemons_bp.route('', methods=["GET", "POST"])
def index():
    pokemon_component = PokemonComponent()
    if request.form:
        pokemon_component.create_pokemon(data=request.form)
    pokemons = pokemon_component.get_all()
    return render_template('pokemon/index.html', pokemons=pokemons)


@pokemons_bp.route('new')
def new():
    return render_template('pokemon/new.html')


@pokemons_bp.route('/update/<int:id>', methods=["POST"])
def update(id):
    if request.form:
        count = PokemonComponent().update_pokemon(pokemon_id=id, data=request.form)
    # if we want to display message, successfully updated, check count = 1
    return redirect(url_for('pokemons.index'))


@pokemons_bp.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    count = PokemonComponent().delete_pokemon(pokemon_id=id)
    # if we want to display message, successfully deleted, check count = 1
    return redirect(url_for('pokemons.index'))


@pokemons_bp.route('/show/<int:id>', methods=["GET"])
def show(id):
    pokemon = PokemonComponent().get_by_id(pokemon_id=id)
    return render_template('pokemon/show.html', pokemon=pokemon)


@pokemons_bp.route('<int:id>/edit')
def edit(id):
    pokemon = PokemonComponent().get_by_id(pokemon_id=id)
    return render_template('pokemon/edit.html', pokemon=pokemon)
