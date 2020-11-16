Cypress.Commands.add('seed', () => {
  cy.exec('cd ../backend && pipenv run python manage.py seed')
})
