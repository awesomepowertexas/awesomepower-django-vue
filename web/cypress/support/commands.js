Cypress.Commands.add('seed', () => {
  cy.exec('cd ../backend && poetry run python manage.py seed')
})
