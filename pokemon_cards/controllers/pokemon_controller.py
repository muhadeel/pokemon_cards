from flask import render_template, request, redirect, url_for, Blueprint
from app.repositories.pokemon_repository import PokemonRepository

pokemons_bp = Blueprint('pokemons', __name__)


@pokemons_bp.route('', methods=["GET", "POST"])
def index():
    if request.form:
        PokemonRepository().create_record(create_data={'name': request.form.get('name')})
    pokemons = PokemonRepository().get_records()
    return render_template('pokemon/index.html', pokemons=pokemons)


@pokemons_bp.route('new')
def new():
    return render_template('pokemon/new.html')


@pokemons_bp.route('/update/<int:id>', methods=["POST"])
def update(id):
    PokemonRepository().update_record(record_id=id, update_data={'name': request.form.get('name')})
    return redirect(url_for('pokemons.index'))


@pokemons_bp.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    PokemonRepository().delete_record(record_id=id)
    return redirect(url_for('pokemons.index'))


@pokemons_bp.route('/show/<int:id>', methods=["GET"])
def show(id):
    pokemon = PokemonRepository().get_by_id(record_id=id)
    return render_template('pokemon/show.html', pokemon=pokemon)


@pokemons_bp.route('<int:id>/edit')
def edit(id):
    pokemon = PokemonRepository().get_by_id(record_id=id)
    return render_template('pokemon/edit.html', pokemon=pokemon)
