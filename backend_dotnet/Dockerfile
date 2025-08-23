# Use the official .NET SDK image to build the app
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /source

# Copy the project file and restore dependencies
COPY TicketSystem.Api/*.csproj ./TicketSystem.Api/
RUN dotnet restore ./TicketSystem.Api/TicketSystem.Api.csproj

# Copy the rest of the app's source code
COPY . .

# Build and publish the app
RUN dotnet publish ./TicketSystem.Api/TicketSystem.Api.csproj -c Release -o /app/publish

# Use the official ASP.NET runtime image to run the app
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

# Expose port 8080 and set the ASP.NET Core URLS environment variable
EXPOSE 8080
ENV ASPNETCORE_URLS=http://+:8080

ENTRYPOINT ["dotnet", "TicketSystem.Api.dll"]
