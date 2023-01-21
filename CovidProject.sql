
--likely hood of dying in a country
select location, date, total_cases, total_deaths, (total_cases/total_deaths)*100 AS DeathPercentage
from CovidDeaths



---total cases vs population
---Shows what percentage of population got covid

select location, date, total_cases, population, (total_cases/population)*100 AS DeathPercentage
from CovidDeaths

---looking at countries with high infection rates compared to population

select location, population, MAX(total_cases) AS HighestInfectionCount, MAX((total_cases/population))*100 AS percentPopulationInfected
from CovidDeaths
--where location like '%states%' 
group by location, population
order by percentPopulationInfected desc

--showing countries deaths by population

select location, population, total_deaths, (total_deaths/population)*100 AS DeathTotalPerc
from CovidDeaths
group by location, population,total_deaths
order by DeathTotalPerc desc

--highest death count per population
select location, population, MAX(cast(total_deaths as int)) AS HighestDeathCount --MAX((total_deaths/population))*100 AS percentdead
from CovidDeaths
--where location like '%states%' 
where continent is not null
group by location, population
order by HighestDeathCount desc

----Breaking down by continent 

select continent, MAX(cast(total_deaths as int)) AS HighestDeathCount --MAX((total_deaths/population))*100 AS percentdead
from CovidDeaths
--where location like '%states%' 
where continent is not null
group by continent
order by HighestDeathCount desc



--countries highest death count per population

select location, MAX(cast(total_deaths as int)) as TotalDeathCount
from CovidDeaths
--where location like '%states%' 
where continent is null
group by location
order by TotalDeathCount desc

---Global Numbers by date

select date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPerecentage
from CovidDeaths
where continent is not null
Group by date
order by 1,2 

-- joining vaccines and deaths tables together
Select*
from CovidDeaths dea  join CovidVaccine vac on 
dea.location = vac.location and dea.date = vac.date


--- Total population vaccinated

select dea.continent, dea.location, dea.date, dea.[population], vac.new_vaccinations,
SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.date)
from CovidDeaths dea  join CovidVaccine vac on 
dea.location = vac.location and dea.date = vac.date
where dea.continent is not null
order by 2,3



-----Using CTE
with PopvsVac (Continent, location, date, Population, New_Vaccinations, RollingPeopleVaccinated)
as 
(
select dea.continent, dea.location, dea.date, dea.[population], vac.new_vaccinations,
SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.date) 
as RollingPeopleVaccinated
from CovidDeaths dea  join CovidVaccine vac on 
dea.location = vac.location and dea.date = vac.date
where dea.continent is not null
)

Select *, (RollingPeopleVaccinated/Population)*100
From PopvsVac

--- Temp table



Drop table if exists #PercentPopulationVaccinated
Create table #PercentPopulationVaccinated
(

Continent nvarchar(255),
location nvarchar(255),
date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
Insert into #PercentPopulationVaccinated
select dea.continent, dea.location, dea.date, dea.[population], vac.new_vaccinations,
SUM(cast(vac.new_vaccinations as int)) OVER (Partition by dea.location Order by dea.location, dea.date) 
as RollingPeopleVaccinated
from CovidDeaths dea  join CovidVaccine vac on 
dea.location = vac.location and dea.date = vac.date
where dea.continent is not null

Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated


---Creating view for visuals

Create view DeathCount as 
select location, MAX(cast(total_deaths as int)) as TotalDeathCount
from CovidDeaths
--where location like '%states%' 
where continent is null
group by location
--order by TotalDeathCount desc
  
Create view HighestDeathCount as --highest death count per population
select location, population, MAX(cast(total_deaths as int)) AS HighestDeathCount --MAX((total_deaths/population))*100 AS percentdead
from CovidDeaths
--where location like '%states%' 
where continent is not null
group by location, population
--order by HighestDeathCount desc

Create view GlobalNumbers as 
select date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPerecentage
from CovidDeaths
where continent is not null
Group by date
--order by 1,2 