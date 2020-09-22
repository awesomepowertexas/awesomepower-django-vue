Cypress.Commands.add('seed', () => {
  cy.exec(
    'cd ../backend' +
      ' && pipenv run python manage.py flush --no-input' +
      ' && pipenv run python manage.py seed',
  )
})
